# Download status

| Dataset | Target | Status |
|---------|--------|--------|
| VocalSet | `raw/vocalset/` (~2.0 GB zip + extract) | **done** (~3615 WAVs) |
| GTSinger English | `raw/gtsinger/English/` (~8.7 GB, ~25k files) | **in progress** (background HF download) |

## When complete

```powershell
cd C:\Users\shagg\Documents\GitHub\Music-producer\datasets\singing

# Re-run is safe (skips completed work)
python scripts\download_datasets.py

# Prepare for RVC-style training (mono, trim, 40 kHz)
python scripts\prepare_for_training.py --format rvc --source vocalset
python scripts\prepare_for_training.py --format rvc --source gtsinger-en

# Manifest for DiffSinger-style pipelines
python scripts\prepare_for_training.py --format diffsinger --source all
```

## Speed tips

- Set `HF_TOKEN` (Hugging Face free account) to avoid 429 rate limits on GTSinger.
- Full multi-language GTSinger: `python scripts\download_datasets.py --all-gtsinger`
