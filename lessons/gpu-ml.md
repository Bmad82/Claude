lessons gpu-ml | maschinen-only | schema: wall_signatur | kategorie | fix | kontext | quelle

wall_signatur | torch.cuda.mem_get_info free total bytes, get_device auto cuda cpu, _cuda_state mockbar, "No device provided using cpu"
kategorie | gpu-ml/device-detection
fix | auto prueft free_gb>=threshold | cuda erzwingt gpu mit cpu-fallback bei ImportError/kein cuda | cpu ueberspringt | get_device()-funktion isolieren, _cuda_state() als mockbares hilfs-api
kontext | sonst sind tests gpu-abhaengig oder brauchen torch als test-dependency
quelle | Zerberus P111

wall_signatur | pip install torch zieht +cpu, torch.cuda.is_available False trotz nvidia-treiber, --index-url cu121
kategorie | gpu-ml/install
fix | pip install torch --index-url https://download.pytorch.org/whl/cu121 (passende cuda-version) | verify: pip list | grep torch, "+cpu" = cpu-only
kontext | ohne cuda-torch bleibt is_available immer False
quelle | Zerberus P111

wall_signatur | SentenceTransformer CrossEncoder device= im konstruktor, inspect.signature verifizieren
kategorie | gpu-ml/sentence-transformers
fix | device im konstruktor: SentenceTransformer("m", device="cuda"), CrossEncoder("m", max_length=512, device="cuda") | per inspect.signature(CrossEncoder.__init__) pruefen
kontext | ab sentence-transformers>=2.2, keine nachtraegliche .to(device) noetig
quelle | Zerberus P111

wall_signatur | cross-encoder cpu 30+ chunks 30-50s, sse-timeout retry-sturm, "No device provided using cpu"
kategorie | gpu-ml/performance
fix | bei latenz zuerst pruefen ob modell auf cpu statt gpu laeuft (log "No device provided, using cpu") | gpu = 5-10x speedup
kontext | cross-encoder auf vielen chunks
quelle | Zerberus P111

wall_signatur | vram-budget whisper 4gb bert-sentiment 0.5 minilm 0.5 bge-reranker 1gb, 8gb karte priorisieren quantisieren
kategorie | gpu-ml/vram
fix | vram planen: whisper ~4gb, bert ~0.5, minilm ~0.5, bge-reranker-v2-m3 ~1gb | 12gb→alles parallel, 8gb→priorisieren/quantisieren
kontext | modelle gleichzeitig resident
quelle |

wall_signatur | nvidia-smi "CUDA Version 13.1" = treiber-max nicht toolkit, torch cu124 auf 13.1-treiber
kategorie | gpu-ml/cuda
fix | nvidia-smi CUDA-version = max vom treiber unterstuetzte runtime, nicht die installierte toolkit-version | aeltere cuda-runtime laeuft auf neuerem treiber
kontext | driver ist rueckwaertskompatibel zu aelteren cuda-runtimes
quelle | Zerberus P111b

wall_signatur | torch force-reinstall typing_extensions 4.9, cryptography>=46 verlangt >=4.13.2, "ImportError cannot import name TypeIs"
kategorie | gpu-ml/deps
fix | nach jeder torch-cuda-install sofort pip install --upgrade "typing-extensions>=4.13.2"
kontext | torch zieht zu altes typing_extensions, andere pakete verlangen neueres
quelle | Zerberus P111b

wall_signatur | "+cu124" suffix pip list gpu-wheel, torch nackt/+cpu cpu-only, pip show torch "package not found -orch" windows file-lock
kategorie | gpu-ml/verify
fix | pip list ist der proof: "2.5.1+cu124"=gpu-wheel, nackt/"+cpu"=cpu-only | waehrend force-reinstall zeigt pip show temporaer "not found" (windows-rename), erst nach completion verlaesslich
kontext | gpu-install verifizieren
quelle | Zerberus P111b
