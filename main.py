# main.py

from src.preprocessing import preprocess_text
from src.fuzzy_search import vector_search, fuzzy_search
from src.relationship_extraction import extract_relationships
from src.hypergraph_builder import build_hypergraph, visualize_hypergraph

def main():
    # Preprocess the text data
    sentences = preprocess_text('data/DSM.txt')
    
    # Test the output sentences
    print("Sample Sentences:")
    for i, sentence in enumerate(sentences[:10]):  # Adjust the number as needed
        print(f"{i+1}: {sentence}")
    
    # Ask for the search query
    query = input("\nEnter your search query: ")
    
    # Perform a semantic search
    top_matches_semantic = vector_search(query, sentences)
    print("\nSemantic Search Top Matches:")
    for match, score in top_matches_semantic:
        print(f"- {match} (Score: {score:.2f})")
    
    # Perform a fuzzy search
    top_matches_fuzzy = fuzzy_search(query, sentences)
    print("\nFuzzy Search Top Matches:")
    for match, score, index in top_matches_fuzzy:
        print(f"- {match} (Score: {score:.2f})")
    
    # Extract relationships
    relationships = extract_relationships(sentences)
    print("\nExtracted Relationships:")
    for subj, verb, obj in relationships[:10]:  # Display first 10 for brevity
        print(f"{subj} --{verb}--> {obj}")
    
    # Build and visualize the hypergraph
    H = build_hypergraph(relationships)
    visualize_hypergraph(H)

if __name__ == "__main__":
    main()
