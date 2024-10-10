def check_operation(nums):
    if len(nums) == 2 and nums[0] != "" and nums[1] != "":
        exp1 = formatting_expression(nums[0])
        exp2 = formatting_expression(nums[1])
        if exp1.isdigit() and exp2.isdigit():
            return True
    return False

def formatting_expression(exp):
    check_point_ind = exp.find(".")
    if check_point_ind != -1:
        if check_point_ind != len(exp) - 1 and check_point_ind != 0 and exp.count(".") == 1:
            return exp[0:check_point_ind] + exp[check_point_ind + 1 :]
        return "f"
    return exp

def formatting_result(res):
    res = str(res)
    if res[len(res) - 1] == "0" and res[len(res) - 2] == ".":
        return res[0 : len(res) - 2]
    return res

def error_output():
    print("Input error!")

def calculating(inp, operation):
    nums = inp.split(operation)
    if check_operation(nums):
        if operation == "+":
            return float(nums[0]) + float(nums[1])
        if operation == "*":
            return float(nums[0]) * float(nums[1])
        if operation == "-":
            return float(nums[0]) - float(nums[1])
        if (("." in nums[1] and nums[1].count("0") == len(nums[1]) - 1)
                or (nums[1].count("0") == len(nums[1]))):
            print("You can't divide by zero!")
            return "zero"
        return float(nums[0]) / float(nums[1])
    try:
        return eval(inp)
    except:
        return "f"

if __name__ == "__main__":
    while True:
        inp_user = input(">> ")
        expression = inp_user.strip()
        expression = expression.replace(" ", "")
        if "+" in expression or "-" in expression or "*" in expression or "/" in expression:
            if "+" in expression:
                result = formatting_result(calculating(expression, "+"))
                if result == "f":
                    error_output()
                    break
                print("{0} = {1}".format(inp_user, result))
            elif "-" in expression:
                result = formatting_result(calculating(expression, "-"))
                if result == "f":
                    error_output()
                    break
                print("{0} = {1}".format(inp_user, result))
            elif "*" in expression:
                result = formatting_result(calculating(expression, "*"))
                if result == "f":
                    error_output()
                    break
                print("{0} = {1}".format(inp_user, result))
            elif "/" in expression:
                result = formatting_result(calculating(expression, "/"))
                if result == "f":
                    error_output()
                    break
                if result == "zero":
                    continue
                print("{0} = {1}".format(inp_user, result))
        elif expression.lower() == "e" or expression.lower() == "exit" or expression == "":
            print("Have a good time of day!")
            break
        else:
            error_output()
            break