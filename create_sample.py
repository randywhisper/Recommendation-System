if __name__ == "__main__":
    f = open("yelp_dataset/yelp_academic_dataset_review.json")
    g = open("yelp_dataset/yelp_academic_dataset_review_sample.json","w+")
    i = 0
    for line in f:
        if i < 100000:
            g.write(line)
        i+=1

    f.close()
    g.close()

