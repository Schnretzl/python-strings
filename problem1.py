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