from contextlib import nullcontext

obj_empty = False
obj_present = True

near_shore_farmer = obj_present
near_shore_fox = obj_present
near_shore_goose = obj_present
near_shore_corn = obj_present


far_shore_farmer = obj_empty
far_shore_fox = obj_empty
far_shore_goose = obj_empty
far_shore_corn = obj_empty

# Sequence of Items Examined
farmer_ind = 0
fox_ind = farmer_ind + 1
goose_ind = fox_ind + 1
corn_ind = goose_ind + 1

# Initial Conditions
near_shore_array = [near_shore_farmer,
                    near_shore_fox, near_shore_goose, near_shore_corn]
far_shore_array = [far_shore_farmer,
                   far_shore_fox, far_shore_goose, far_shore_corn]

max_objects = len(near_shore_array)

failed_scenario = False

# Message Strings
# --1-- Messages
success_message = "Items Transported Successfully"
failed_message = "Items still missing or transported unsuccessfully"
incomplete_message = "Items still missing in journey from far."

goose = "Goose"
fox = "Fox"
corn = "Corn"
farmer = "Farmer"

fox_and_goose_message = "The Fox has eaten the Goose!"
goose_and_corn_message = "The Goose has eaten the corn!"


journey_sequence = [

    farmerCrossesRiver(goose_ind)  # N2F
    farmerCrossesRiver()           # F2N
    farmerCrossesRiver(fox_ind)    # N2F
    farmerCrossesRiver(goose_ind)  # F2N
    farmerCrossesRiver(corn_ind)   # N2F
    farmerCrossesRiver()           # F2N
    farmerCrossesRiver(goose_ind)  # N2F

]

# Journey


def takeItemsOver(journey_arr):

    while failed_scenario == False:

        for path in journey_arr:

            checkConstraints(near_shore_array, far_shore_array)
            journey_arr[path]

            # Needs a loop breaker statement when the far shore is full.

    if failed_scenario == True:

        return failed_message

    for object_present in far_shore_array:

        if far_shore_array[object_present] == False:

            return failed_message

    return success_message

# Constraints Validation


def checkConstraints():

    # Check the near shore array if the farmer isn't there, otherwise check the far shore array.
    array_to_check = near_shore_array if near_shore_array[
        farmer_ind] != obj_present else far_shore_array

    # If the fox is on the boat, the goose and corn better not be alone...
    if array_to_check[fox_ind] != obj_present:

        if array_to_check[goose_ind] == array_to_check[corn_ind]:

            print(goose_and_corn_message)
            failed_scenario = True

    # If the corn is on the boat, the fox and goose better not be alone...
    if array_to_check[corn_ind] != obj_present:

        if array_to_check[fox_ind] == array_to_check[goose_ind]:

            print(fox_and_goose_message)
            failed_scenario = True


def farmerCrossesRiver(item_ind=farmer_ind):

    indexUpperBound = max_objects - 1
    indexLowerBound = farmer_ind

    if item_ind > indexUpperBound or item_ind < indexLowerBound:

        return

    # Checks to see if the farmer is taking something with him
    if item_ind != farmer_ind:

        near_shore_array[item_ind], far_shore_array[item_ind] = far_shore_array[item_ind], near_shore_array[item_ind]

    # Farmer crosses each time
    near_shore_array[farmer_ind], far_shore_array[farmer_ind] = far_shore_array[farmer_ind], near_shore_array[farmer_ind]
