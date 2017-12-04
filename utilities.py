# Script for universal utilities

# Strips symbols before sending to TTS Agent
def stripSymbols(s):
    s = s.replace("&",' y ').strip()
    s = s.replace("%",' porciento ').strip()
    s = s.replace("-",' ').strip()
    s = s.replace("*",' asterisco ').strip()
    s = s.replace("#",' almohadilla ').strip()
    s = s.replace("@",' en ').strip()
    s = s.replace("'",'').strip()
    return s
    
