{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "d3d4f91d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 1\n",
      "Empty list\n",
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 2\n",
      "What is your task? Cooking\n",
      "What is the deadline? Monday\n",
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 1\n",
      "9c703cce-0787-4673-a9a5-a93abcb3f68f | Cooking | Monday\n",
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 3\n",
      "Enter ID to complete: 9c703cce-0787-4673-a9a5-a93abcb3f68f\n",
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 1\n",
      "Empty list\n",
      "\n",
      "    == TODO LIST ==\n",
      "    [1] show task\n",
      "    [2] add task\n",
      "    [3] complete task\n",
      "    [4] exit\n",
      "    \n",
      "Your choice: 4\n",
      "Have a good day!\n"
     ]
    }
   ],
   "source": [
    "#TO DO LIST FULL CODE\n",
    "import uuid\n",
    "\n",
    "def main_menu():\n",
    "    \n",
    "    global choice\n",
    "    \n",
    "    print(\"\"\"\n",
    "    == TODO LIST ==\n",
    "    [1] show task\n",
    "    [2] add task\n",
    "    [3] complete task\n",
    "    [4] exit\n",
    "    \"\"\")\n",
    "        \n",
    "    choice = str(input(\"Your choice: \"))\n",
    "\n",
    "\n",
    "class todo_list():\n",
    "    \n",
    "    def add_task(self):\n",
    "        self.temp_str = []\n",
    "        \n",
    "        self.idd = str(uuid.uuid4())\n",
    "        self.temp_str.append(self.idd)\n",
    "        \n",
    "        self.task = input(\"What is your task? \")\n",
    "        self.temp_str.append(self.task)\n",
    "        \n",
    "        self.deadline = input(\"What is the deadline? \")\n",
    "        self.temp_str.append(self.deadline)\n",
    "    \n",
    "        try:\n",
    "            stream = open('todo_list.txt', 'a')\n",
    "            for i in range(len(self.temp_str)):\n",
    "                if i != 2:\n",
    "                    stream.write(self.temp_str[i])\n",
    "                    stream.write(\" | \")\n",
    "                else:\n",
    "                    stream.write(self.temp_str[i])\n",
    "                    stream.write(\"\\n\")\n",
    "            stream.close()\n",
    "        except Exception as e:\n",
    "            print('An error occurred:', e)\n",
    "            \n",
    "    def show_task(self):\n",
    "        try:\n",
    "            stream = open('todo_list.txt', 'r')\n",
    "            lines = stream.readlines()\n",
    "            if lines != []:\n",
    "                for line in lines:\n",
    "                    print(line, end='')\n",
    "                stream.close()\n",
    "            else:\n",
    "                print('Empty list')\n",
    "        except Exception as e:\n",
    "            print('An error occurred:', e)\n",
    "            \n",
    "    def remove_task(self):\n",
    "        self.temp_list2 = []\n",
    "        self.remove = input(\"Enter ID to complete: \")\n",
    "        \n",
    "        try:\n",
    "            stream = open('todo_list.txt', 'r')\n",
    "            lines = stream.readlines()\n",
    "        \n",
    "            for line in lines:\n",
    "                if self.remove not in line:\n",
    "                    self.temp_list2.append(line)\n",
    "            \n",
    "            stream = open('todo_list.txt', 'w')\n",
    "            for i in self.temp_list2:\n",
    "                stream.write(i)\n",
    "            stream.close()\n",
    "        except Exception as e:\n",
    "            print('An error occurred:', e)\n",
    "        \n",
    "        \n",
    "arman_list = todo_list()\n",
    "choice = 0\n",
    "\n",
    "while choice != '4':\n",
    "    main_menu()\n",
    "    if choice == '1':\n",
    "        arman_list.show_task()\n",
    "    elif choice == '2':\n",
    "        arman_list.add_task()\n",
    "    elif choice == '3':\n",
    "        arman_list.remove_task()\n",
    "    else:\n",
    "        break\n",
    "\n",
    "print('Have a good day!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e33d6e3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
