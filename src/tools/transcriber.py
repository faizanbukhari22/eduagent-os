import os
from faster_whisper import WhisperModel

def transcribe_audio_file(audio_path: str) -> str:
    """Loads a pre-baked model from the local image footprint and runs transcription."""
    # Read the container environment variable path
    baked_root = os.getenv("WHISPER_MODEL_PATH", "/app/models")
    
    print(f"[Transcriber] Initializing local Whisper model (base) from: {baked_root}...")
    
    # Pass 'base' as the model name signature, and isolate the storage directory
    model = WhisperModel(
        model_size_or_path="base",
        device="cpu",
        compute_type="int8",
        download_root=baked_root if os.path.exists(baked_root) else None
    )
    
    print(f"[Transcriber] Processing audio timeline for: {os.path.basename(audio_path)}")
    segments, info = model.transcribe(audio_path, beam_size=5)
    
    transcript_segments = []
    for segment in segments:
        transcript_segments.append(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text}")
        
    return "\n".join(transcript_segments)
