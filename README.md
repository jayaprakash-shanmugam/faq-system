# Enterprise FAQ System

AI-powered FAQ system with hybrid search capabilities (semantic + keyword).

## Installation

### From PyPI
```bash
pip install enterprise-faq-system
```

### From TestPyPI (for testing new versions)
```bash
pip install -i https://test.pypi.org/simple/ enterprise-faq-system==0.1.0 --extra-index-url https://pypi.org/simple
```

## Usage

```python
from faq_system.core import ProductionFAQSystem

# Initialize
faq = ProductionFAQSystem()

# Add FAQs
faq.load_knowledge_base()

# Search
results = faq.answer_question("Tell me about AI")
print(results)
```

## Development

1. Clone the repo:
```bash
git clone https://github.com/jayaprakash-shanmugam/faq-system.git
cd faq-system
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Publishing to PyPI

1. Build the package:
```bash
python -m build
```

2. Upload to TestPyPI:
```bash
twine upload --repository testpypi dist/*
```

3. Upload to PyPI:
```bash
twine upload dist/*
```

## License

[MIT License](LICENSE)
