
import random







def calc_priorities(presentation_numb):
    group_presentations_priority_values = {}
    max_priority = 0
    for i in groups:
        priority = 0
        if presentation_numb in preferences[i-1]:
            presentation_group_index = preferences[i-1].index(presentation_numb)
            priority = (presentations_count - presentation_group_index) * 10
        if (max_priority < priority):
            max_priority = priority
        group_presentations_priority_values[i] = priority
    return group_presentations_priority_values, max_priority # key value :
    # {group_num : priority_point_for_presentation{presentation_index}}

def calc_presentation_popularity():
    presentations_popularity = {}
    for pres in presentations:
        pres_popularity = 0
        for gp in groups:
            if (pres in preferences[gp - 1]):
                pres_popularity += (max_priority_count - preferences[gp - 1].index(pres)) ** 2
        presentations_popularity[pres] = pres_popularity
    return sorted(presentations_popularity.items(), key=lambda x:x[1], reverse= True)
    # return sorted(presentations_popularity.items(), key=lambda x:x[1], reverse= False)
    # {group_num : priority_point_for_presentation{presentation_index}}

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    presentations_count = 10
    copy_groups_count = groups_count = 5
    max_priority_count = 10
    preferences = []
    print("########Preferences##################")
    # test data
    for i in range(groups_count):
        preference = random.sample(range(1, 11), 10)
        preferences.append(preference)
        print(i+1, ": ", preference)

    # read from text


    # with open("preferences_group_4.txt", 'r') as f:
    #     lines = f.readlines()
    #
    #
    # for e in lines:
    #     e = e.replace('\n', '')
    #     e = e.split(',')
    #     pref = [int(n) for n in e]
    #     preferences.append(pref)
    #
    #
    # for i in range(groups_count):
    #     print(i+1, ": ", preferences[i])

    print("###################################")
    group_presentations = {}
    groups = [i for i in range(1,groups_count+1)]
    presentations = [i for i in range(1, presentations_count+1)]

    sorted_presentations_by_popularity = calc_presentation_popularity()
    print("(subject_number, popularity_point)")
    print("sorted_presentations_by_popularity : ", sorted_presentations_by_popularity)
    print("###################################")
    for pres in sorted_presentations_by_popularity:
        i = pres[0]
        priority_point_for_presentation, max_priority_for_presentation = calc_priorities(i)
        volunteers = []
        for gp_pri_key in priority_point_for_presentation.keys():
            if priority_point_for_presentation[gp_pri_key] == max_priority_for_presentation:
                volunteers.append(gp_pri_key)
        winner = volunteers[random.randint(0, len(volunteers)-1)]
        group_presentations[winner] = i
        groups.remove(winner)
        groups_count -= 1
        if (groups_count <= 0):
            break





    # for i in presentations:
    #     priority_point_for_presentation, max_priority_for_presentation = calc_priorities(i)
    #     volunteers = []
    #     for gp_pri_key in priority_point_for_presentation.keys():
    #         if priority_point_for_presentation[gp_pri_key] == max_priority_for_presentation:
    #             volunteers.append(gp_pri_key)
    #     winner = volunteers[random.randint(0, len(volunteers)-1)]
    #     group_presentations[winner] = i
    #     groups.remove(winner)
    #     groups_count -= 1




    print("{group_number : subject_number}")
    print("group_presentations : " , group_presentations)
    # print(len(group_presentations))
    print("###################################")

    groups_satisfaction = {}
    for key in group_presentations.keys():
        satisfaction = 0
        if (group_presentations[key] in preferences[key - 1]):
            satisfaction = (max_priority_count - preferences[key - 1].index(group_presentations[key]) ) / max_priority_count
        groups_satisfaction[key] = satisfaction
    print("{group_number : satisfaction rate}")
    print("groups_satisfaction : ", groups_satisfaction)
    print("###################################")
    print("satisfaction rate mean : ", (sum(groups_satisfaction.values())) / copy_groups_count)
    print("###################################")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
