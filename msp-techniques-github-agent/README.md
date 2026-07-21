# Theory and Technique of Electronic Music (Puckette) GitHub Agent

Separate agent for **Miller Puckette, *The Theory and Technique of Electronic Music*** (World Scientific, 2007).

**Source:** https://msp.ucsd.edu/techniques/latest/book.pdf  

Pd-oriented computer music theory + technique (oscillators → FFT & classical waves).

## Layout

| Path | Purpose |
|------|---------|
| `AGENTS.md` | System prompt |
| `msp_kb/` | Chapters, concepts, recipes |
| `knowledge/Theory_and_Technique_of_Electronic_Music.pdf` | Local PDF (~337 pages) |
| `knowledge/manual_extract.txt` | Full text extract |

## Chapters (1–10)

1. Sinusoids, amplitude and frequency  
2. Wavetables and samplers  
3. Audio and control computations  
4. Automation and voice management  
5. Modulation  
6. Designer spectra  
7. Time shifts and delays  
8. Filters  
9. Fourier analysis and resynthesis  
10. Classical waveforms  

## CLI

```bash
cd msp-techniques-github-agent
python -m msp_kb info
python -m msp_kb list-chapters
python -m msp_kb chapter 7
python -m msp_kb define paf
python -m msp_kb recipe fm_basic
python -m msp_kb search "phase vocoder"
```

## Notes

- Run examples in **Pure Data** (included with Pd distribution).  
- © World Scientific / author rights apply. Agent scaffolding for local study only.
