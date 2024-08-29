# Problem 1: 1. Product Review Analysis

# Task 1: Keyword Highlighter
def keyword_highlighter(reviews, keywords = ["good", "excellent", "bad", "poor", "average"]):
    for review in reviews:
        lower_review = review.replace(review, review.lower())
        keyword_index, keyword_length = None, 0
        for keyword in keywords:
            if keyword in lower_review:
                keyword_index = lower_review.find(keyword)
                keyword_length = len(keyword)
                break
            #end if
        #end for
        
        print(review if keyword_index is None else review[0:keyword_index] + keyword.upper() + review[keyword_index + keyword_length:])
    #end for
#end function            
    
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keyword_highlighter(reviews)


#Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"],\
                    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]):
    positive_count, negative_count = 0, 0
    for review_num in range(len(reviews)):
        lower_review = reviews[review_num].lower()
        for word in positive_words:
            positive_count += lower_review.count(word)
        #end for
        for word in negative_words:
            negative_count += lower_review.count(word)
        #end for
        
        print(f"Review {review_num + 1}:\n\t-Positive: {positive_count}\n\t-Negative: {negative_count}")
        positive_count, negative_count = 0, 0
    #end for
        
sentiment_tally(reviews)


#Task 3: Review Summary
def review_summary(review):
    if len(review) <= 30:
        return review
    #end if
    
    review_words = review.split()
    truncated_review = ""
    while len(truncated_review) + len(review_words[0]) < 30:
        truncated_review += review_words.pop(0) + " "
    #end while
    
    return truncated_review.strip() + "..."
#end function

long_review = "Here is a very long review that needs to be cut off because it goes on for so long and nobody wants to read it all."
print(review_summary(long_review))