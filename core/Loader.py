import pkgutil
import importlib
import plugins

def load_plugins():
    loaded = []

    for module in pkgutil.iter_modules(plugins.__path__):
        name = module.name
        mod = importlib.import_module(f"plugins.{name}")

        if hasattr(mod, "Plugin"):
            loaded.append(mod.Plugin())

    return loaded
