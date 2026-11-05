$ErrorActionPreference = 'Stop'
Write-Host '== Run AIMS-mini =='
py main.py
if ($LASTEXITCODE -ne 0) { throw 'main.py failed' }
Write-Host "`n== Run unit tests =="
py -m unittest discover -s tests -v
if ($LASTEXITCODE -ne 0) { throw 'Unit tests failed' }
Write-Host "`nAll local checks passed."
