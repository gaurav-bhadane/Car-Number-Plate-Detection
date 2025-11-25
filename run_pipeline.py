from agents.agent_orchestrator import OrchestratorAgent

if __name__ == "__main__":
    image = "test.jpg"   # change your path

    orch = OrchestratorAgent()
    response = orch.execute(image)

    print(response)