from data_transform import data_transform as dt
from collections import Counter
from collections import OrderedDict
import math

#def user_based_cf(data):



def matrix_user_based(raw_data,business):
    user_dict = {}
    for rev in raw_data:
        if rev["user_id"] in user_dict:
            user_dict[rev["user_id"]][rev["business_id"]] = int(rev["stars"])
        else:
            user_dict[rev["user_id"]] = {rev["business_id"]:int(rev["stars"])}

    user_dict = OrderedDict(sorted(user_dict.items(),key = lambda x: x[0]))
    matrix = []
    for user,value in user_dict.items():
        matrix_value = []
        for bus in business:
            if bus in value:
                matrix_value.append(value[bus])
            else:
                matrix_value.append(.0)
        matrix.append(matrix_value)
    return matrix

def matrix_item_based(raw_data,user):
    item_dict = {}
    for rev in raw_data:
        if rev["business_id"] in item_dict:
            item_dict["business_id"][rev["user_id"]] = int(rev["stars"])
        else:
            item_dict["business_id"] = {rev["user_id"]:int(rev["stars"])}

    item_dict = sorted(item_dict.items(),key = lambda x: x[0])
    matrix = []
    for business,value in item_dict.items():
        matrix_value = []
        for u in uesr:
            if u in value:
                matrix_value.append(value[u])
            else:
                matrix_value.append(.0)
        matrix.append(matrix_value)
    return matrix


def similarity_cos(vector_x,vector_y):
    top = (float)sum([x*y for x,y in zip(vector_x,vector_y)])
    bottom = math.sqrt(sum([x**2 for x in vector_x])) * math.sqrt(sum([y**2 for y in vector_y]))
    similarity = top/bottom
    return similarity


def user_based_cf(custom,user,matrix,n,m):

    recommend_list = []
    index = user.index(custom) 
    list_sim = []
    for i in xrange(len(user)):
        if i != index:
            sim = similarity_cos(matrix[i],matrix[index])
            list_sim.append([i,sim])
        else:
            continue
    top = sorted(list_sim,key = lambda x:x[1])[:n] 

    for key,value in enumerate(matrix[index]):
        if value == 0.0:
            predict_val = 0
            div_sum = 0
            for user_top in top:
               if matrix[user_top[0]][key] != 0:
                   predict_val += matrix[user_top[0]][key]*user_top[1]
                   div_sum += user_top[1]
            predict_val /= div_sum
            recommend_list.append([key,predict_val])
        else:
            continue
   return sorted(recommend_list,key = lambda x:x[1],reverse = True)[:m] 

def item_based_cf(custom,user,business,matrix,n,m):
    index = user.index(custom)
    matrix = numpy.array(matrix)
    star_item = list(matrix[:,index])
    for key,item in enumerate(star_item):
        if item != 0:


if __name__ == "__main__":

    review = dt("yelp_dataset/yelp_academic_dataset_review.json")
    review_data = review.tran_json()

    user = []
    business = []
    for rev in raw_data::
        if rev["user_id"] in user::
            pass
        else:
            user.append(rev["user_id"])
        if rev["business_id"] in business:
            pass
        else:
            business.append(rev["business_id"])
    business.sort()
    user.sort()


    user_based_cf
