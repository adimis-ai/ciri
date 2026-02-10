import urllib.request
import json

def fetch_and_filter_models():
    url = "https://openrouter.ai/api/v1/models"
    try:
        with urllib.request.urlopen(url, timeout=30.0) as response:
            if response.status != 200:
                print(f"Error: Status code {response.status}")
                return
            data = json.loads(response.read().decode()).get("data", [])
        
        filtered = []
        for model in data:
            context = model.get("context_length", 0)
            if context < 150000:
                continue
                
            arch = model.get("architecture", {})
            input_modalities = arch.get("input_modalities", [])
            # Some models might not have architecture field or input_modalities
            has_vision = "image" in input_modalities or "vision" in str(model.get("description", "")).lower()
            
            supported_params = model.get("supported_parameters", [])
            has_tools = "tools" in supported_params or "functions" in supported_params
            
            if has_vision and has_tools:
                filtered.append({
                    "id": model.get("id"),
                    "name": model.get("name"),
                    "context": context,
                    "vision": has_vision,
                    "tools": has_tools,
                    # description is often very long, let's keep it concise
                })
        
        print(json.dumps(filtered, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_and_filter_models()
