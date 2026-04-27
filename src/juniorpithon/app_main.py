import uvicorn
import logging

def launch():
    logging.info("[*] Igniting JuniorPiThon IDE Ecosystem...")
    uvicorn.run("juniorpithon.terminals.dynamic_dashboard:app", host="0.0.0.0", port=8080, reload=True)

if __name__ == "__main__":
    launch()
