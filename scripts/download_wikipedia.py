import wikipediaapi

def fetch_wikipedia_article(topic, save_path):
    try:
        wiki = wikipediaapi.Wikipedia(
            user_agent="KakeruApp/1.0 (https://github.com/kakeru/study-app)", 
            language='en'
        )
        page = wiki.page(topic)
        if not page.exists():
            print(f"❌ Error: '{topic}' not found on Wikipedia.")
            return
        
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(page.text)
        
        print(f"✅ Saved: {save_path}")
    except Exception as e:
        print(f"❌ Error: {e}")

topics = ["Mathematics", "Statistics", "Biology", "Chemistry", "Physics", 
          "Computer Science", "Artificial Intelligence", "History", 
          "Literature", "Business", "Economics"]

for topic in topics:
    fetch_wikipedia_article(topic, f"datasets/raw_texts/{topic.replace(' ', '_')}.txt")
