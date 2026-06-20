# Deployment Guide

## Local Development

### Prerequisites
- Python 3.8 or higher
- pip or conda package manager
- Git

### Setup Steps

1. **Clone Repository**
```bash
git clone https://github.com/amananandsingh01/ai-for-good.git
cd ai-for-good
```

2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run Tests**
```bash
pytest tests/
```

5. **Run Examples**
```bash
python examples/education_example.py
python examples/healthcare_example.py
python examples/agriculture_example.py
python examples/arts_example.py
```

## Docker Deployment

### Build Docker Image
```bash
docker build -t ai-for-good:latest .
```

### Run Container
```bash
docker run -p 8000:8000 ai-for-good:latest
```

## Production Deployment

### Environment Variables
Create `.env` file with necessary configurations:
```
DEBUG=False
AGENT_TIMEOUT=30
LOG_LEVEL=INFO
DATABASE_URL=postgresql://user:password@localhost/ai_for_good
```

### API Server Setup
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Database Setup
```bash
alembic upgrade head
```

### Monitoring and Logging
- Implement logging with structured logs
- Set up monitoring with Prometheus
- Configure alerts for critical errors

## Cloud Deployment

### AWS
- Use EC2 or ECS for container orchestration
- RDS for managed database
- CloudWatch for monitoring

### Google Cloud
- Deploy on Cloud Run or GKE
- Cloud SQL for database
- Cloud Logging for monitoring

### Azure
- Deploy on Container Instances or AKS
- Azure Database for PostgreSQL
- Azure Monitor for observability

## Performance Tuning

- Cache frequently accessed data
- Implement connection pooling
- Use async processing for long-running tasks
- Monitor resource usage
- Implement rate limiting

## Security Considerations

- Use environment variables for sensitive data
- Implement API authentication (JWT, OAuth2)
- Validate and sanitize all inputs
- Use HTTPS/TLS for all communications
- Regular security audits and updates
- Implement CORS properly

## Backup and Recovery

- Regular database backups
- Backup code repositories
- Document recovery procedures
- Test recovery procedures regularly

## CI/CD Pipeline

Use GitHub Actions for automated testing and deployment:
```yaml
name: Deploy
on: [push]
jobs:
  test-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run tests
        run: pytest
      - name: Deploy
        run: ./deploy.sh
```

## Scaling Strategies

1. **Horizontal Scaling**: Deploy multiple agent instances
2. **Caching**: Use Redis for caching
3. **Load Balancing**: Distribute traffic across instances
4. **Database Optimization**: Index frequently queried fields
5. **Async Processing**: Use task queues for long operations

## Troubleshooting

### Common Issues

**Issue: Import errors**
```bash
# Solution: Reinstall dependencies
pip install --force-reinstall -r requirements.txt
```

**Issue: Database connection errors**
```bash
# Solution: Check DATABASE_URL and connection settings
python -c "from sqlalchemy import create_engine; engine = create_engine('postgresql://...')"
```

**Issue: Agent timeout**
- Increase AGENT_TIMEOUT in environment variables
- Optimize agent processing logic
- Implement request queueing

## Support

For deployment issues:
1. Check logs: `docker logs container_id`
2. Review error messages
3. Consult documentation
4. Open an issue on GitHub