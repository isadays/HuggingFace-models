from transformers import pipeline

def translate_to_swedish():
    translator = pipeline(task='translation', model='facebook/nllb-200-distilled-600M', torch_dtype="auto")
    
    print("Enter a word or phrase to translate into Swedish (type 'exit' to quit):")
    
    while True:
        user_input = input("Your input: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            translation = translator(user_input, src_lang="pt_Latn", tgt_lang="swe_Latn")
            print(f"Translation in Swedish: {translation[0]['translation_text']}")
        except Exception as e:
            print(f"Error occurred during translation: {e}")

if __name__ == "__main__":
    translate_to_swedish()
