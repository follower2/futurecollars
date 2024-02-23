# lesson2 15-2-24
def main():
    max_items = int(input("Enter the number of items to be shipped: "))
    
    packages_sent = 0
    total_weight_sent = 0
    max_unused_capacity = 0
    max_unused_capacity_package_number = 0
    
    current_package_weight = 0
    unused_capacity = 0
    
    package_number = 1
    
    while True:
        item_weight = float(input(f"Enter the weight of item (kg) {package_number}: "))
        
        if item_weight == 0:
            print(f"{item_weight} cannot be 0 (kg)")
            break
        
        if current_package_weight + item_weight > 20:
# Mark current package as sent
            packages_sent += 1
            total_weight_sent += current_package_weight
            unused_capacity = 20 - current_package_weight
            if unused_capacity > max_unused_capacity:
                max_unused_capacity = unused_capacity
                max_unused_capacity_package_number = package_number - 1
            
# Start a new package with the current item
            current_package_weight = item_weight
            package_number += 1
        else:
            current_package_weight += item_weight
        
        if package_number > max_items:
            print("Maximum number of items reached.")
            break
    
# Check if there's an unsent package
    if current_package_weight > 0:
        packages_sent += 1
        total_weight_sent += current_package_weight
    
    print("Number of packages sent:", packages_sent)
    print("Total weight of packages sent:", total_weight_sent, "kg")
    print("Total 'unused' capacity:", (packages_sent * 20) - total_weight_sent, "kg")
    print("Package number with the most 'unused' capacity:", max_unused_capacity_package_number)
    print("Amount of 'unused' capacity in that package:", max_unused_capacity, "kg")

if __name__ == "__main__":
    main()