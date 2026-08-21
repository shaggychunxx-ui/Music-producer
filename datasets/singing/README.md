# Singing voice datasets (training)

Local store for free research corpora used to train / fine-tune a **singing generator**.

## Layout

```text
datasets/singing/
  raw/
    vocalset/     # VocalSet (CC BY 4.0) — techniques, ~10h
    gtsinger/     # GTSinger (CC BY-NC-SA 4.0) — multi-lang, large
  prepared/
    rvc/          # flat WAVs for RVC-style voice training
    diffsinger/   # segment lists / metadata for SVS pipelines
  scripts/
    download_datasets.py
    prepare_for_training.py
```

**Large audio is gitignored.** Only scripts + this README are meant for git.

## Datasets

| Name | License | Notes |
|------|---------|--------|
| [VocalSet](https://zenodo.org/records/1193957) | CC BY 4.0 | 20 singers, technique takes; ~2 GB zip |
| [GTSinger](https://huggingface.co/datasets/AaronZ345/GTSinger) | CC BY-NC-SA 4.0 | **Non-commercial**; multi-language, scores, techniques |

Always re-read each project's license before commercial use.

## Download

```powershell
cd C:\Users\shagg\Documents\GitHub\Music-producer\datasets\singing
python scripts\download_datasets.py              # VocalSet + GTSinger English
python scripts\download_datasets.py --all-gtsinger  # full GTSinger (very large)
python scripts\download_datasets.py --vocalset-only
python scripts\download_datasets.py --gtsinger-only
```

## Prepare for training

```powershell
# RVC-style: collect dry-ish WAVs, optional silence trim + mono + resample
python scripts\prepare_for_training.py --format rvc --source vocalset
python scripts\prepare_for_training.py --format rvc --source gtsinger-en
python scripts\prepare_for_training.py --format rvc --source all

# Manifest only (paths + duration) for DiffSinger-style tooling
python scripts\prepare_for_training.py --format diffsinger --source all
```

## Training tips

- Prefer **dry mono** vocals; strip heavy reverb/doubles when possible.
- RVC / clone: **10–30+ minutes** of one singer beats random multi-singer soup.
- Full multi-technique SVS: use GTSinger annotations (TextGrid / json / musicxml in raw tree).
- Do **not** train on commercial sample packs or copyrighted acapellas without rights.
