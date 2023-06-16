


touch Task_ToDo.txt Removed_Task.txt Done_Task.txt

add_task() {
    echo "Enter task description:"
    read description
    echo "Enter task priority (1-3):"
    read priority
    echo "Enter task due date (YYYY-MM-DD):"
    read due_date
    if grep -q "^$description," Task_ToDo.txt; then
        echo "Error: Task already exists in ToDo list"
    else
        echo "$description,$priority,$due_date" >> Task_ToDo.txt
        echo ""
        echo "Task added successfully!"
    fi
    echo ""
    echo "-------------------------------"
    echo ""
}


remove_task() {
    echo "Enter task description to remove:"
    read description
    if grep -q "^$description," Task_ToDo.txt; then
        sed -i "/^$description,/d" Task_ToDo.txt
        echo "$description,$(date +%Y-%m-%d_%H:%M:%S)" >> Removed_Task.txt  # date +%Y-%m-%d_%H:%M:%S ---> year-month-day_hour:minute:second
        echo ""
        echo "Task removed successfully!"
    elif grep -q "^$description," Removed_Task.txt; then
        echo "Error: Task already removed"
    elif grep -q "^$description," Done_Task.txt; then
        echo "Error: Task already marked as done"
    else
        echo "Error: Task not found in ToDo list"
    fi
    echo ""
    echo "-------------------------------"
    echo ""
}


mark_done() {
    echo "Enter task description to mark as done:"
    read description
    if grep -q "^$description," Task_ToDo.txt; then
        sed -i "/^$description,/d" Task_ToDo.txt
        echo "$description,$(date +%Y-%m-%d_%H:%M:%S)" >> Done_Task.txt
        echo ""
        echo "Task marked as done successfully!"
        echo ""
    elif grep -q "^$description," Removed_Task.txt; then
        echo "Error: Task already removed"
        echo ""
    elif grep -q "^$description," Done_Task.txt; then
        echo "Error: Task already marked as done"
        echo ""
    else
        echo "Error: Task not found in ToDo list"
        echo ""
    fi
    echo ""
    echo "-------------------------------"
    echo ""
}

search_task() {
    echo "Enter task description to search for:"
    echo ""
    read description
    if grep -q "^$description," Task_ToDo.txt; then
        echo ""
        echo "Task found in ToDo list"
        echo ""
    elif grep -q "^$description," Removed_Task.txt; then
        echo ""
        echo "Task found in Removed list"
        echo ""
    elif grep -q "^$description," Done_Task.txt; then
        echo ""
        echo "Task found in Done list"
        echo ""
    else
        echo ""
        echo "Task not found"
        echo ""
    fi
}


while true; do
    echo "Select an option:"
    echo "1. <Add a task>"
    echo "2. <Remove a task>"
    echo "3. <Mark a task as done>"
    echo "4. <Search for a task>"
    echo "5. <Exit>"
    echo ""
    echo "Option:"
    read choice

    case $choice in
        1) add_task;;
        2) remove_task;;
        3) mark_done;;
        4) search_task;;
        5) echo "Exiting ToDo program !"; exit;;
        *) echo "Invalid choice, please try again !";;
    esac
done
