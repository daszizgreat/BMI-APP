import mysql.connector
import webbrowser
import random
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')

def add_user():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2511DASis@@",
        database="fitgraph"
    )

    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT, email VARCHAR(100), weight FLOAT, height FLOAT)")

    num_users = int(input("Enter the number of users you want to add: "))

    for i in range(num_users):
        print(f"\nUser {i+1}:")
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        email = input("Enter your email: ")
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))

        insert_query = "INSERT INTO users (name, age, email, weight, height) VALUES (%s, %s, %s, %s, %s)"
        user_data = (name, age, email, weight, height)
        cursor.execute(insert_query, user_data)

        print("User information saved successfully!")

    conn.commit()

    cursor.close()
    conn.close()
def open_random_link():
    links = [
        "https://www.youtube.com/watch?v=WE50ZSVQeDs",
        "https://www.youtube.com/watch?v=JjvN_hYDp3g",
        "https://www.youtube.com/watch?v=_JRefJH6N00&pp=ygUabW90aXZhdGlvbiBleGVyY2lzZXMgdmlkZW8%3D",
        "https://www.youtube.com/watch?v=Y5RtQ4cawVk&pp=ygUabW90aXZhdGlvbiBleGVyY2lzZXMgdmlkZW8%3D",
        "https://www.youtube.com/watch?v=oAM6H2LqT6A&pp=ygUabW90aXZhdGlvbiBleGVyY2lzZXMgdmlkZW8%3D"
    ]
    random_link = random.choice(links)
    webbrowser.open(random_link)

def find_user_by_name(name):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2511DASis@@",
        database="fitgraph"
    )

    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = %s"
    cursor.execute(query, (name,))

    user = cursor.fetchone()

    if user:
        print("User found:")
        print(f"Name: {user[1]}")
        print(f"Age: {user[2]}")
        print(f"Email: {user[3]}")
        print(f"Weight: {user[4]} kg")
        print(f"Height: {user[5]} meters")

        weight = user[4]  
        height = user[5]  

        bmi = calculate_bmi(weight, height)
        bmi_interpretation = interpret_bmi(bmi)
        print(f"You are {bmi_interpretation}.")

       

        generate_dishes_and_select_random(bmi_interpretation)
    else:
        print("User not found!")

   

def remove_all_users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="2511DASis@@",
        database="fitgraph"
    )

    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")

    conn.commit()

    print("All users removed successfully!")

    cursor.close()
    conn.close()

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    
     
    print(f"Your BMI is: {bmi}")
    show_graph_option = input("Do you want to show the BMI graph? (yes/no): ").lower()
    if show_graph_option == "yes":
        plot_bmi_graph(bmi)  
    exercise_option = input("Do you want exercise suggestions based on your BMI category? (yes/no): ").lower()
    if exercise_option == "yes":
        bmi_category = interpret_bmi(bmi)
        exercise_suggestion = suggest_exercises(bmi_category)
        print("Exercise Suggestions based on your BMI category:\n", exercise_suggestion)
    else:
        print("Thank you!")

    return bmi

def suggest_exercises(bmi_category):
    if bmi_category == "underweight":
        return "You should focus on bulking exercises. Here are 30 bulking exercises:\n1. Push-ups for Upper-body Strength\n2. Pull-ups: Effective for Arm and Back Muscles\n3. Lunges for Leg and Glute Muscles.\n4. Overhead Press for Shoulder Development.\n5. Barbell Curls for Biceps Strength.\n6. Planks for Core Strength.\n7. Bench Press for Upper-body Strength.\n8. Dumbbell Rows for Back Muscles.\n9. Squats\n10. Deadlifts\n11. Barbell Bench Press for Chest Development.\n12. Dumbbell Shoulder Press for Shoulder Strength and Size.\n13. Bent-over Rows for Back and Arm Muscles.\n14. Barbell Squats for Lower Body Strength and Size.\n15. Barbell Lunges for Leg and Glute Development.\n16. Barbell Hip Thrusts for Glute Activation and Strength.\n17. Arnold Press for Shoulder Muscles.\n18. Dumbbell Chest Flyes for Pectoral Muscles.\n19. Barbell Romanian Deadlifts for Hamstring and Lower Back Strength.\n20. Chin-ups for Upper Back and Biceps.\n21. Cable Rows for Back Muscles and Core Stability.\n22. Leg Press for Quadriceps and Glute Development.\n23. Tricep Dips for Tricep Strength and Definition.\n24. Bulgarian Split Squats for Leg Strength and Stability.\n25. Incline Bench Press for Upper Chest Development.\n26. Seated Dumbbell Shoulder Press for Shoulder Muscles.\n27. Barbell Calf Raises for Calf Muscle Growth.\n28. Cable Crunches for Abdominal Strength and Definition.\n29. Farmer's Walk for Grip Strength and Overall Muscular Development.\n30. Lat Pulldowns for Back Muscles and Upper Body Strength."
    elif bmi_category == "normal weight":
        return "You should focus on full body workouts. Here are 30 full body workout exercises:\n1. Star Jumps (3 x 20)\n2. Squats (3 x 15)\n3. Push-ups (3 x 10)\n4. Lunges (3 x 15 on each leg)\n5. Plank (As many sets as it takes to get to 2 minutes)\n6. Side plank (1 minute each side)\n7. Step-ups (3 x 10 on each leg)\n8. Chair dips (3 x 10)\n9. Wall sit (3 x 30 seconds)\n10. Pull-ups (Bodyweight for one)\n11. Burpees (3 x 10)\n12. Mountain climbers (3 x 20)\n13. Russian twists (3 x 20)\n14. Deadlifts (3 x 12)\n15. Jumping lunges (3 x 12 on each leg)\n16. Bicycle crunches (3 x 20)\n17. Tricep push-ups (3 x 10)\n18. Superman (3 x 15)\n19. Box jumps (3 x 10)\n20. Russian kettlebell swings (3 x 15)\n21. Renegade rows (3 x 10 on each arm)\n22. Jump squats (3 x 15)\n23. Reverse lunges with knee drive (3 x 12 on each leg)\n24. Hanging leg raises (3 x 12)\n25. Bear crawl (3 x 20 meters)\n26. Spiderman push-ups (3 x 10)\n27. Plank with shoulder taps (3 x 15 on each side)\n28. Turkish get-ups (3 x 8 on each side)\n29. Stability ball rollouts (3 x 12)\n30. Battle rope waves (3 x 20 seconds)"
    elif bmi_category == "obese":
        return "You should focus on cardio exercises. Here are 30 cardio exercises:\n1. Sprinting\n2. Jump rope\n3. Burpee\n4. Mountain climbers.\n5. Squat jumps\n6. Jumping jack\n7. Stair climbing\n8. Swimming\n9. Cycling\n10. Dance\n11. High knees\n12. Box jumps\n13. Rowing\n14. Kickboxing\n15. Elliptical training\n16. Running stairs\n17. Hiking\n18. Jumping lunges\n19. Shadow boxing\n20. Plyometric push-ups\n21. Treadmill running\n22. Inline skating\n23. Jump squats\n24. Zumba\n25. Battle rope exercises\n26. Cross-country skiing\n27. Jumping hurdles\n28. Cardio kickboxing\n29. Jumping on a trampoline\n30. Rowing machine sprints"
    else:
        return "Invalid BMI category"




def interpret_bmi(bmi):
    # Interpret BMI
    if bmi < 18.5:
        return "underweight"
    elif bmi >= 18.5 and bmi < 25:
        return "normal weight"
    else:
        return "obese"



def plot_bmi_graph(bmi):
    categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]

    bmi_ranges = [(0, 18.5), (18.5, 25), (25, 30), (30, 100)]

    colors = ['blue', 'green', 'orange', 'red']

    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    for i in range(len(categories)):
        plt.axvspan(bmi_ranges[i][0], bmi_ranges[i][1], color=colors[i], alpha=0.3)
        plt.text((bmi_ranges[i][0] + bmi_ranges[i][1]) / 2, 0.5, categories[i], ha='center', fontsize=12, weight='bold')
    plt.axvline(x=bmi, color='black', linestyle='--', linewidth=2)
    plt.text(bmi, 0.6, f'Your BMI: {bmi}', rotation=90, ha='right', fontsize=12, weight='bold')
    plt.xlabel('BMI')
    plt.ylabel('Category')
    plt.title('BMI Scale')
    plt.xlim(0, 40)
    plt.ylim(0, 1)
    plt.xticks(range(0, 41, 5))
    plt.yticks([]) 
    plt.grid(False)

    plt.subplot(1, 3, 2)
    bar_categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
    bar_counts = [5, 15, 10, 8] 
    plt.bar(bar_categories, bar_counts, color=colors)
    plt.xlabel('BMI Category')
    plt.ylabel('Number of People')
    plt.title('BMI Distribution')
    plt.grid(axis='y')

    plt.subplot(1, 3, 3)
    pie_categories = ["Underweight", "Normal Weight", "Overweight", "Obese"]
    pie_sizes = [5, 15, 10, 8]  
    plt.pie(pie_sizes, labels=pie_categories, colors=colors, autopct='%1.1f%%')
    plt.title('BMI Distribution')

    plt.tight_layout()
    plt.show()


normal_breakfast = [
    "Whole grain toast with avocado and poached egg", 
    "Greek yogurt with granola and mixed fruit", 
    "Whole wheat pancakes with maple syrup and berries",
    "Oatmeal with sliced bananas and honey",
    "Scrambled eggs with spinach and feta cheese",
    "Smoothie bowl with spinach, banana, and almond butter",
    "Breakfast burrito with scrambled eggs, black beans, and salsa",
    "Egg muffins with vegetables and cheese",
    "Quinoa porridge with almond milk and dried fruits",
    "Vegetable omelette with whole wheat toast",
    "Banana walnut muffins with Greek yogurt",
    "Cottage cheese with sliced peaches and almonds",
    "Avocado toast with smoked salmon and capers",
    "Fruit salad with cottage cheese",
    "Whole grain waffles with fresh strawberries",
    "Shakshuka (poached eggs in tomato sauce)",
    "Chia seed pudding with mixed berries",
    "Peanut butter and banana sandwich on whole wheat bread",
    "Breakfast tacos with scrambled eggs and avocado",
    "Vegetable frittata with arugula salad",
    "Breakfast quesadilla with scrambled eggs, cheese, and salsa",
    "Breakfast parfait with yogurt, granola, and berries",
    "Sourdough toast with ricotta and honey",
    "Apple cinnamon oatmeal with walnuts",
    "Egg and cheese bagel sandwich",
    "Pumpkin pancakes with cinnamon yogurt sauce",
    "Vegetable hash with poached eggs",
    "Blueberry almond smoothie",
    "English muffin with scrambled eggs and Canadian bacon",
    "Muesli with yogurt and sliced kiwi"
]


normal_lunch = [
    "Grilled chicken Caesar salad with whole grain croutons", 
    "Quinoa salad with chickpeas, cucumber and feta cheese", 
    "Vegetable stir-fry with tofu and brown rice",
    "Turkey and avocado wrap with lettuce and tomato",
    "Mediterranean couscous salad with grilled vegetables",
    "Caprese salad with fresh mozzarella, tomatoes, and basil",
    "Sushi rolls with brown rice, avocado, and cucumber",
    "Lentil soup with whole grain bread",
    "Greek salad with olives, tomatoes, and feta cheese",
    "Turkey and cranberry sandwich on whole wheat bread",
    "Vegetable and bean burrito bowl with salsa and guacamole",
    "Chicken and vegetable curry with quinoa",
    "Grilled shrimp skewers with quinoa tabbouleh",
    "Egg salad sandwich with whole grain crackers",
    "Vegetable and tofu pad thai",
    "Black bean and corn salad with lime vinaigrette",
    "Tuna salad with mixed greens and balsamic dressing",
    "Vegetarian chili with cornbread",
    "Pita pockets with hummus, cucumber, and tomato",
    "Salmon and avocado sushi bowl with brown rice",
    "Mushroom and barley soup with whole grain bread",
    "Pesto pasta salad with cherry tomatoes and mozzarella",
    "Vegetable and lentil curry with brown rice",
    "Chicken Caesar wrap with romaine lettuce and Parmesan cheese",
    "Vegetable and chickpea tagine with couscous",
    "Tofu and vegetable stir-fry with soba noodles",
    "Roast beef and cheddar sandwich on whole grain bread",
    "Tomato basil soup with grilled cheese sandwich",
    "Greek-style stuffed peppers with quinoa and feta",
    "Shrimp and avocado salad with citrus vinaigrette"
]



normal_dinner = [
    "Chicken Alfredo pasta with garlic bread and Caesar salad", 
    "Beef stir-fry with noodles and vegetables", 
    "Cheese stuffed meatballs with marinara sauce and spaghetti",
    "Grilled salmon with roasted potatoes and steamed broccoli",
    "Vegetable curry with brown rice",
    "Pesto chicken with roasted vegetables",
    "Turkey meatloaf with mashed sweet potatoes and green beans",
    "Shrimp scampi with angel hair pasta",
    "Honey glazed pork chops with quinoa and roasted Brussels sprouts",
    "Vegetarian lasagna with garlic bread",
    "Lemon herb roasted chicken with wild rice pilaf",
    "Baked tilapia with asparagus and couscous",
    "Mushroom risotto with Parmesan cheese",
    "Teriyaki tofu with stir-fried vegetables and rice noodles",
    "Grilled steak with baked sweet potato and sautéed spinach",
    "Lentil soup with crusty whole grain bread",
    "Pork tenderloin with roasted carrots and mashed potatoes",
    "Spinach and ricotta stuffed shells with marinara sauce",
    "Honey mustard glazed salmon with quinoa salad",
    "Vegetable curry with naan bread",
    "Sesame ginger tofu with jasmine rice and steamed bok choy",
    "Grilled shrimp skewers with pineapple salsa and brown rice",
    "Eggplant Parmesan with spaghetti and marinara sauce",
    "Black bean enchiladas with Spanish rice and guacamole",
    "Stuffed bell peppers with ground turkey and quinoa",
    "Soy-glazed cod with sesame broccoli and jasmine rice",
    "Creamy mushroom chicken with roasted potatoes",
    "Vegetable paella with saffron rice",
    "Baked ziti with marinara sauce and garlic bread"
]




obese_breakfast = [
    "Whole grain pancakes with maple syrup and sliced bananas", 
    "Omelette with cheese, bacon, and hash browns", 
    "French toast with powdered sugar and strawberries",
    "Breakfast burrito with scrambled eggs, cheese, sausage, and potatoes",
    "Blueberry muffins with streusel topping",
    "Breakfast sandwich with sausage, egg, cheese, and biscuit",
    "Chocolate chip pancakes with whipped cream",
    "Sausage and cheese biscuits with gravy",
    "Cinnamon rolls with cream cheese frosting",
    "Bagel breakfast sandwich with cream cheese, bacon, and avocado",
    "Belgian waffles with whipped cream and chocolate sauce",
    "Bacon, egg, and cheese croissant sandwich",
    "Breakfast pizza with scrambled eggs, bacon, and cheese",
    "Banana bread with chocolate chips",
    "Sausage gravy and biscuits",
    "Peanut butter chocolate chip oatmeal",
    "Loaded breakfast nachos with eggs, bacon, cheese, and salsa",
    "Caramel apple cinnamon rolls",
    "Fried chicken and waffles with syrup",
    "Cheese and sausage breakfast casserole",
    "Blueberry cream cheese stuffed French toast",
    "Egg and cheese breakfast sliders with sausage patties",
    "Cinnamon sugar donuts",
    "Breakfast tacos with scrambled eggs, chorizo, and cheese",
    "Apple pie oatmeal with caramel sauce",
    "Breakfast quesadilla with scrambled eggs, cheese, bacon, and avocado",
    "Brown sugar cinnamon pancakes with whipped cream",
    "Fried eggs with bacon and hash brown casserole",
    "Chocolate chip banana bread muffins"
]
obese_lunch = [
    "Cheeseburger with fries and a milkshake", 
    "Fried chicken sandwich with coleslaw and fries", 
    "Buffalo wings with ranch dressing and celery sticks",
    "Double bacon cheeseburger with onion rings",
    "BBQ pulled pork sandwich with macaroni and cheese",
    "Philly cheesesteak with loaded potato wedges",
    "Fish and chips with tartar sauce",
    "Meat lover's pizza with extra cheese and pepperoni",
    "Chili cheese fries with sour cream and jalapenos",
    "Chicken tenders basket with fries and honey mustard sauce",
    "Bacon-wrapped hot dogs with chili and cheese",
    "Pulled beef brisket sandwich with potato salad",
    "Deep-fried shrimp basket with hush puppies and coleslaw",
    "Loaded nachos with beef, cheese, and guacamole",
    "Cheesy bacon ranch potato skins",
    "Garlic parmesan chicken wings with blue cheese dressing",
    "Sausage and pepperoni calzone with marinara dipping sauce",
    "Pork belly tacos with refried beans and Spanish rice",
    "Grilled cheese sandwich with tomato soup",
    "Beef and bean burritos with nacho cheese sauce",
    "Cheese stuffed pretzels with mustard dipping sauce",
    "Beef and cheese quesadillas with sour cream and salsa",
    "Baked macaroni and cheese with breadcrumb topping",
    "Loaded potato soup with bacon, cheese, and sour cream",
    "Spicy beef tacos with melted cheese and avocado",
    "Bacon-wrapped jalapeno poppers with cream cheese filling",
    "Fried clam strips with tartar sauce and french fries",
    "Fried mozzarella sticks with marinara dipping sauce",
    "Cheese and bacon loaded potato skins",
    "BBQ pulled chicken sandwich with coleslaw and fries"
]



obese_dinner = [
    "Chicken Alfredo pasta with garlic bread and Caesar salad", 
    "Beef stir-fry with noodles and vegetables", 
    "Cheese stuffed meatballs with marinara sauce and spaghetti",
    "BBQ ribs with baked beans and coleslaw",
    "Meat lover's pizza with extra cheese and pepperoni",
    "Fettuccine Alfredo with garlic breadsticks",
    "Bacon-wrapped meatloaf with mashed potatoes and gravy",
    "Loaded cheeseburger with fries and onion rings",
    "Deep dish pepperoni pizza with cheesy breadsticks",
    "Pulled pork sandwiches with macaroni and cheese",
    "Beef enchiladas with refried beans and Spanish rice",
    "Fried chicken with mashed potatoes and biscuits",
    "Beef and cheese quesadillas with sour cream and guacamole",
    "Sausage and pepperoni calzone with marinara dipping sauce",
    "Bacon-wrapped stuffed chicken with loaded baked potatoes",
    "Cheeseburger macaroni and cheese",
    "Buffalo chicken wings with ranch dressing and celery sticks",
    "Creamy bacon carbonara with garlic bread",
    "Beef and bean burritos with nacho cheese sauce",
    "Cheeseburger sliders with seasoned fries",
    "Baked ziti with Italian sausage and garlic bread",
    "Loaded baked potato soup with cheese and bacon",
    "Three cheese lasagna with garlic bread",
    "Shrimp and sausage jambalaya with cornbread",
    "Barbecue pulled pork pizza with coleslaw",
    "Creamy chicken and bacon Alfredo with garlic bread",
    "Cheese steak sandwiches with onion rings",
    "Garlic butter shrimp scampi with linguine",
    "Beef and bacon-loaded baked potatoes",
    "Teriyaki glazed salmon with fried rice"
]


underweight_breakfast = [
    "Scrambled eggs with avocado toast", 
    "Greek yogurt with mixed berries and honey", 
    "Whole grain toast with almond butter and banana slices",
    "Smoothie with spinach, banana, and protein powder",
    "Cottage cheese with pineapple chunks and almonds",
    "Egg and vegetable breakfast wrap",
    "Oatmeal with sliced strawberries and chopped nuts",
    "Whole grain cereal with low-fat milk and sliced peaches",
    "Fruit and nut granola with yogurt",
    "Peanut butter and jelly sandwich on whole wheat bread",
    "Avocado and tomato omelette with whole grain toast",
    "Banana and almond butter smoothie",
    "Ricotta cheese with sliced pears and honey",
    "Quinoa porridge with dried fruits and nuts",
    "Whole wheat English muffin with cottage cheese and berries",
    "Vegetable and cheese frittata with whole grain toast",
    "Chia seed pudding with mango and coconut flakes",
    "Whole grain bagel with smoked salmon and cream cheese",
    "Vegetable and tofu stir-fry with brown rice",
    "Apple cinnamon oatmeal with walnuts and raisins",
    "Muesli with yogurt and sliced kiwi",
    "Whole grain pancakes with Greek yogurt and blueberries",
    "Baked apple oatmeal with cinnamon and almonds",
    "Whole wheat waffles with strawberries and yogurt",
    "Spinach and cheese breakfast quesadilla",
    "Banana and spinach smoothie with protein powder",
    "Whole grain muffin with cottage cheese and fruit",
    "Veggie and cheese omelette with whole wheat toast",
    "Fruit salad with low-fat cottage cheese",
    "Almond milk oatmeal with sliced almonds and dried cranberries"
]


underweight_lunch = [
    "Avocado and turkey wrap with spinach and tomato", 
    "Grilled chicken salad with mixed greens and balsamic vinaigrette", 
    "Quinoa salad with chickpeas, cucumber, and feta cheese",
    "Hummus and vegetable sandwich on whole grain bread",
    "Tuna salad with mixed greens and lemon vinaigrette",
    "Caprese salad with tomatoes, mozzarella, and basil",
    "Vegetable and bean burrito with salsa and avocado",
    "Mango and shrimp salad with citrus dressing",
    "Turkey and cranberry sandwich on whole wheat bread",
    "Vegetable stir-fry with tofu and brown rice",
    "Egg salad sandwich on whole grain bread with spinach",
    "Greek yogurt chicken salad with grapes and almonds",
    "Miso soup with tofu and seaweed salad",
    "Pita bread stuffed with falafel and tzatziki sauce",
    "Vegetable and lentil soup with whole grain crackers",
    "Salmon and avocado sushi rolls with miso soup",
    "Chicken Caesar wrap with romaine lettuce and Parmesan cheese",
    "Spinach and mushroom quesadilla with salsa verde",
    "Chicken and vegetable stir-fry with noodles",
    "Tomato and basil bruschetta with whole grain bread",
    "Vegetable and chickpea curry with naan bread",
    "Turkey and avocado panini with mixed greens",
    "Mediterranean pasta salad with olives and feta cheese",
    "Shrimp and avocado salad with citrus vinaigrette",
    "Vegetarian sushi rolls with edamame",
    "Chicken and vegetable teriyaki bowl with brown rice",
    "Spinach and feta stuffed peppers with quinoa",
    "Vegetable and tofu pad thai with peanuts",
    "Mushroom and goat cheese flatbread with arugula salad"
]


underweight_dinner = [
    "Grilled chicken breast with sweet potato and steamed asparagus", 
    "Salmon fillet with quinoa pilaf and roasted Brussels sprouts", 
    "Vegetable and tofu curry with brown rice",
    "Baked cod with lemon herb butter and sautéed spinach",
    "Turkey meatballs with marinara sauce and spaghetti squash",
    "Stir-fried shrimp with vegetables and rice noodles",
    "Baked chicken thighs with roasted root vegetables",
    "Vegetable and chickpea stew with crusty whole grain bread",
    "Grilled shrimp skewers with pineapple salsa and jasmine rice",
    "Turkey chili with kidney beans and cornbread",
    "Miso-glazed tofu with stir-fried bok choy and udon noodles",
    "Chicken and vegetable stir-fry with quinoa",
    "Baked tilapia with mango salsa and cilantro lime rice",
    "Vegetable and lentil curry with coconut milk and naan bread",
    "Shrimp and vegetable kebabs with herbed couscous",
    "Honey mustard glazed salmon with roasted vegetables",
    "Turkey and vegetable stir-fry with brown rice",
    "Stuffed bell peppers with quinoa and black beans",
    "Grilled steak with roasted potatoes and green beans",
    "Mushroom risotto with Parmesan cheese and garlic bread",
    "Baked chicken Parmesan with spaghetti and marinara sauce",
    "Vegetable and chickpea tagine with couscous",
    "Lemon garlic shrimp with angel hair pasta",
    "Vegetable and tofu stir-fry with soba noodles",
    "Baked sweet and sour chicken with jasmine rice",
    "Stuffed acorn squash with quinoa and cranberries",
    "Grilled turkey burgers with sweet potato fries",
    "Vegetable and black bean enchiladas with Spanish rice",
    "Lemon herb grilled fish with quinoa salad",
    "Mushroom and spinach stuffed chicken breast with roasted potatoes"
]


# Store dishes for each BMI category
dish_categories = {
    "underweight": {
        "Breakfast": underweight_breakfast,
        "Lunch": underweight_lunch,
        "Dinner": underweight_dinner
    },
    "normal weight": {
        "Breakfast": normal_breakfast,
        "Lunch": normal_lunch,
        "Dinner": normal_dinner
    },
    "obese": {
        "Breakfast": obese_breakfast,
        "Lunch": obese_lunch,
        "Dinner": obese_dinner
    }
}

def generate_dishes_and_select_random(weight_category):
    categories = ["Breakfast", "Lunch", "Dinner"]

    random_dishes = [random.choice(dish_categories[weight_category][category]) for category in categories]

    print(f"{weight_category.capitalize()} Meal:")
    for i, dish in enumerate(random_dishes, start=1):
        print(f"{i}. {dish}")





def find_user():
    user_name = input("Enter the name of the user you want to find: ")
    find_user_by_name(user_name)

def remove_users():
    print("Removing all users...")

def motivation_tab():
    print("Opening motivation tab...")
    open_random_link()

def exit_program():
    print("Exiting program.")
    exit()

def switch_case(choice):
    switcher = {
        '1': add_user,
        '2': find_user,
        '3': remove_users,
        '4': motivation_tab,
        '5': exit_program
    }
    selected_function = switcher.get(choice, lambda: print("Invalid choice!"))
    selected_function()

while True:
    choice = input("Enter your choice (1: Add user, 2: Find user, 3: Remove all users, 4: Motivation tab, 5: Exit): ")

    if choice == '5':
        print("Exiting program.")
        break  

    switch_case(choice)
