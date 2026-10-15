# maspy-hello-world

Small playground for experimenting with MASPY agent creation and belief updates.

## Experiments

### 1. Initial belief
Create the agent with the triggering belief already present:

```python
ag = HelloAgent(beliefs=Belief("hello"))
Admin().start_system()
```

### 2. Add belief after creation
Create the agent first, then add the belief before starting the system:

```python
ag = HelloAgent()
ag.add(Belief("hello"))
Admin().start_system()
```