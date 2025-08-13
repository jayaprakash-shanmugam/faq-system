from faq_system import ProductionFAQSystem

def main():
    # Initialize FAQ system
    faq = ProductionFAQSystem()
    faq.load_knowledge_base()
    
    # Test query
    result = faq.answer_question("What is your software?")
    print(f"Answer: {result['answer']}")
    print(f"Confidence: {result['confidence']:.3f}")

if __name__ == "__main__":
    main()