"""
Lazy Loading Fix for ActiveVisionPortal — model_registry.py
============================================================
Problem:
    The original model_registry.py imports ALL models at startup.
    This causes dependency errors even for simple CLI operations
    like --list_models when optional dependencies (e.g. Detectron2)
    are not installed.

Fix:
    Models are imported only when explicitly requested by name.
    All other operations (listing, help, validation) work without
    triggering any model-specific imports.

Author: Apurva Sharma
GSoC 2026 — INCF Project #19 ActiveVision
"""

# ── BEFORE (original behavior — eager loading) ──────────────────
# Every model is imported at the top of the file.
# If Detectron2 is missing, even --list_models fails.

# from models.HAT.entry import HATModel        # fails if Detectron2 absent
# from models.IRL.entry import IRLModel
# from models.DeepGaze.entry import DeepGazeModel

# MODEL_REGISTRY = {
#     "HAT": HATModel,
#     "IRL": IRLModel,
#     "DeepGaze": DeepGazeModel,
# }


# ── AFTER (lazy loading fix) ─────────────────────────────────────
# Models are registered by name and import path only.
# The actual import happens only when the model is requested.

MODEL_REGISTRY = {
    "HAT":      "models.HAT.entry.HATModel",
    "IRL":      "models.IRL.entry.IRLModel",
    "DeepGaze": "models.DeepGaze.entry.DeepGazeModel",
}


def get_model(model_name: str):
    """
    Returns the model class for the given name.
    Import happens here — only when explicitly requested.
    
    Args:
        model_name: Name of the model (e.g. 'HAT', 'IRL')
    
    Returns:
        Model class
    
    Raises:
        ValueError: If model_name is not in the registry
        ImportError: If the model's dependencies are not installed
    """
    if model_name not in MODEL_REGISTRY:
        available = list(MODEL_REGISTRY.keys())
        raise ValueError(
            f"Model '{model_name}' not found. "
            f"Available models: {available}"
        )

    import importlib
    module_path, class_name = MODEL_REGISTRY[model_name].rsplit(".", 1)

    try:
        module = importlib.import_module(module_path)
        model_class = getattr(module, class_name)
        return model_class

    except ImportError as e:
        raise ImportError(
            f"Could not import model '{model_name}'. "
            f"Make sure all dependencies are installed.\n"
            f"Original error: {e}"
        )


def list_models():
    """
    Lists all available models WITHOUT importing any of them.
    This is the key benefit of lazy loading — works even when
    optional dependencies like Detectron2 are not installed.
    """
    return list(MODEL_REGISTRY.keys())


# ── Example usage ────────────────────────────────────────────────
if __name__ == "__main__":
    # This works even without Detectron2 installed
    print("Available models:", list_models())

    # This imports only IRL — not HAT, not DeepGaze
    IRLModel = get_model("IRL")
    print("IRL model loaded:", IRLModel)
