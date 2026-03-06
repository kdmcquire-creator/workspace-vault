""import json

import os

import re

import sys

from datetime import datetime, timezone



import requests

from google.oauth2 import service_account

from googleapiclient.discovery import build



SANITY_API_VERSION = os.getenv("SANITY_API_VERSION", "2025-01-01")





def _env(name: str, required: bool = True, default: str | None = None) -> str:
  
    v = os.getenv(name, default)
  
    if required and not v:
      
        raise RuntimeError(f"Missing env var: {name}")
      
    return v or ""
  




def _slugify(s: str) -> str:
  
    s = (s or "").strip().lower()
  
    s = re.sub(r"[^a-z0-9]+", "-", s)
  
    s = re.sub(r"-+", "-", s).strip("-")
  
    return s
  




def sanity_mutate(project_id: str, dataset: str, token: str, mutations: list[dict]):
  
    url = f"https://{project_id}.api.sanity.io/v{SANITY_API_VERSION}/data/mutate/{dataset}"
  
    r = requests.post(
      
        url,
      
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
      
        json={"mutations": mutations},
      
        timeout=60,
      
    )
  
    if r.status_code >= 300:
      
        raise RuntimeError(f"Sanity mutate failed: {r.status_code} {r.text[:400]}")
      
    return r.json()
  




def fetch_sheet_values(service_account_json: str, sheet_id: str, sheet_range: str):
  
    info = json.loads(service_account_json)
  
    creds = service_account.Credentials.from_service_account_info(
      
        info,
      
        scopes=["https://www.googleapis.com/auth/spreadsheets.readonly"],
      
    )
  
    svc = build("sheets", "v4", credentials=creds, cache_discovery=False)
  
    resp = svc.spreadsheets().values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
  
    return resp.get("values", [])
  




def main():
  
    project_id = _env("SANITY_PROJECT_ID")
  
    dataset = _env("SANITY_DATASET")
  
    token = _env("SANITY_TOKEN")
  


    sa_json = _env("GOOGLE_SERVICE_ACCOUNT_JSON")
  
    sheet_id = _env("GOOGLE_SHEET_ID")
  
    sheet_range = _env("GOOGLE_SHEET_RANGE", default="Tools!A1:Z")
  


    values = fetch_sheet_values(sa_json, sheet_id, sheet_range)
  
    if not values or len(values) < 2:
      
        print("No rows found in sheet range.")
      
        return
      


    headers = [h.strip() for h in values[0]]
  
    rows = values[1:]
  


    def get(row, key, default=""):
      
        try:
          
            idx = headers.index(key)
          
        except ValueError:
          
            return default
          
        return row[idx].strip() if idx < len(row) and isinstance(row[idx], str) else (row[idx] if idx < len(row) else default)
      


    tool_mutations = []
  
    category_mutations = []
  


    # Pre-create categories referenced by tools.

    referenced_categories: set[str] = set()
  


    normalized_rows = []
  
    for r in rows:
      
        name = str(get(r, "name", "")).strip()
      
        slug = str(get(r, "slug", "")).strip() or _slugify(name)
      
        if not slug:
          
            continue
          


        cats = str(get(r, "categories", "")).strip()
      
        cat_slugs = [c.strip() for c in cats.split(


























































