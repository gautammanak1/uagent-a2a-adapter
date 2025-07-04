"""Basic usage example for uAgent A2A Adapter."""

from dotenv import load_dotenv
from uagent_a2a_adapter import A2AAdapter

# Load environment variables
load_dotenv()

# Mock agent executor for demonstration
class MockAgentExecutor:
    """Mock agent executor for demonstration purposes."""
    
    async def execute(self, context, event_queue):
        """Mock execute method."""
        # In a real implementation, this would process the request
        # and add events to the event queue
        pass

def main():
    """Main function to run the basic A2A agent example."""
    # Create a mock executor (replace with your actual executor)
    executor = MockAgentExecutor()
    
    # Create the adapter
    adapter = A2AAdapter(
        agent_executor=executor,
        name="basic_a2a_agent",
        description="A basic A2A agent example",
        port=8082,
        a2a_port=9997,
        mailbox=True,
        seed="basic_example"
    )
    
    print("🚀 Starting Basic A2A Agent...")
    print("📝 This is a basic example of the uAgent A2A Adapter")
    print("🔗 The agent will be available for communication via uAgents protocol")
    print()
    
    # Run the adapter (this will block)
    adapter.run()

if __name__ == "__main__":
    main()
