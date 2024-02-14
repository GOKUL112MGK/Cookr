def interpret_star_rating(star_rating):
    if star_rating >= 4:
        return "excellent"
    elif star_rating == 3:
        return "average"
    else:
        return "poor"

def generate_review_summary(quality_rating, timeliness_rating, quantity_rating):
    quality_review = interpret_star_rating(quality_rating)
    timeliness_review = interpret_star_rating(timeliness_rating)
    quantity_review = interpret_star_rating(quantity_rating)

    summary = "People think that food provided by this kitchen is of"

    if quality_review == "excellent":
        summary += " excellent quality,"
    elif quality_review == "average":
        summary += " average quality,"
    else:
        summary += " poor quality,"

    if timeliness_review == "excellent":
        summary += " timely delivery,"
    elif timeliness_review == "average":
        summary += " average timeliness of delivery,"
    else:
        summary += " delayed delivery,"

    if quantity_review == "excellent":
        summary += " and sufficient quantity of food."
    elif quantity_review == "average":
        summary += " and average quantity of food."
    else:
        summary += " and poor quantity of food."

    return summary

# Get input from the user
quality_rating = float(input("Enter the star rating for quality (1-5): "))
timeliness_rating = float(input("Enter the star rating for timeliness (1-5): "))
quantity_rating = float(input("Enter the star rating for quantity (1-5): "))

review_summary = generate_review_summary(quality_rating, timeliness_rating, quantity_rating)
print(review_summary)