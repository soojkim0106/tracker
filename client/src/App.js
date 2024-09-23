import { useState, useEffect } from "react";
import Header from "./components/Header";
import TaskContainer from "./components/TaskContainer";
import Form from "./components/Form";

function App() {
  const [tasks, setTasks] = useState([]);

  const fetchTasks = () => {
    fetch("/tasks")
      .then((response) => response.json())
      .then((data) => setTasks(data))
      .catch((error) => console.error("Error fetching tasks:", error));
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  const handleUpdateTask = (updatedTask) => {
    fetch(`/tasks/${updatedTask.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updatedTask),
    })
      .then((response) => response.json())
      .then((data) => {
        setTasks(tasks.map((task) => (task.id === data.id ? data : task)));
      })
      .catch((error) => console.error("Error updating task:", error));
  };

  const handleDeleteTask = (taskId) => {
    const confirmDelete = window.confirm(
      "Are you sure you want to delete this task?"
    );
    if (confirmDelete) {
      fetch(`/tasks/${taskId}`, {
        method: "DELETE",
      })
        .then((response) => {
          if (response.ok) {
            setTasks(tasks.filter((task) => task.id !== taskId));
          } else {
            console.error(`Failed to delete task with id ${taskId}.`);
          }
        })
        .catch((error) => console.error("Error deleting task:", error));
    }
  };

  const handleCompleteTask = (taskId) => {
    const updatedTask = tasks.find((task) => task.id === taskId);
    if (updatedTask) {
      updatedTask.status = "Completed";

      fetch(`/tasks/${taskId}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ status: "Completed" }),
      })
        .then((response) => response.json())
        .then((data) => {
          setTasks(tasks.map((task) => (task.id === data.id ? data : task)));
        })
        .catch((error) => console.error("Error completing task:", error));
    }
  };

  const addTask = (newTask) => {
    setTasks([...tasks, newTask]);
  };


  return (
    <>
      <Header />
      <Form addTask={addTask} />
      <TaskContainer
        tasks={tasks}
        onUpdateTask={handleUpdateTask}
        onDeleteTask={handleDeleteTask}
        onCompleteTask={handleCompleteTask}
      />
    </>
  );
}

export default App;
