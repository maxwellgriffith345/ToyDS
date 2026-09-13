### Motivation
- learn more about AI agent frame works
- project: Multi Agent application


### Frameworks
- LangChain
- LangGraph

### Questions
- where do I start in creating my own AI agents? like library etc


### LangChain and LangGraph
[LangChain vs LangGraph](https://www.youtube.com/watch?v=qAF1NjEVHhY)

LangChain
  - build LLM powered applications
  - SEQUENCE of functions in a chain
  - no cycles, directed graph
  - it moves in sequentail steps
  - linear workflow: step1 then step 2 ect
  - chain parts together with functions
  - ie "Retrieve - Summarize - Anaswer"

LangChain
  - stateful multio agent apps/system
  - can handle non-linear workflows
  - ie loops, passing info back and forth between agents
  - "nodes" and "edges"
  - all agents can edit and read from the "state" so all agents work from the same context

Primary Focus
- Langgraph: create and manage multi agent systems and workflows
- LangChain: abstraction layer for chaining LLM operations to LLM apps

Structure
- LangChain: chain/DAG graph, takes are always moving forward
  - greate when you know the exact sequence of steps needed
- LangGraph: Graph
  - allows for loops and revisitng previous states
  - good for interactive systems

Componenets
- LangChain: Memory, Prompt, LLM, Agent which forms chaini
- LangGraph: Nodes, Edges, States

StateManagment
- LangChain: limited state managment, non persistent state
- LangGraph: more robust managment, core comopnent, all nodes can access and edit states

Use Cases:
- LangChain: sequential tasks ie Retrieve data, process it and output it
- LangGraph: complex systems, requiring ongoing interaction



### RAG
[ 7 AI Terms You Need to Know: Agents, RAG, ASI & More ](https://www.youtube.com/watch?v=VSFuqMh4hus&list=PLOspHqNVtKADc8E1JLd_kBBPdEBDdmwsR)
- Retervial augmented generation
- uses vector databases to enrich prompts to an LLM
- Retriever component - takes in a prompt - turns it into an embedding model
- then perform a similarity search in a vector database
- return the results from the search back through the embedding to the user

### MCP
- Model context protocol
- a way for LLMs or agent apps to connect to external systems
- like a database or an email
- it is a standardized way for AI to access your systems

### Terms to learn
- vector database
- MCP
