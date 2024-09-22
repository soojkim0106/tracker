import { useState, useEffect } from 'react';
import Header from './components/Header';
import Form from './components/Form';
import TaskContainer from './components/TaskContainer';

function App() {

  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5555/tasks')
      .then((response) => response.json())
      .then((data) => setTasks(data))
      .catch((error) => console.error('Error fetching goals:', error));
  }, []);

  const addTask = (newTask) => {
    setTasks([...tasks, newTask]);
  }

  const handleEdit = (task) => {
    fetch(`http://localhost:5555/tasks/${task.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ ...task })
    })
      .then((response) => response.json())
      .then((data) => {
        const updatedTasks = tasks.map((t) => {
          if (t.id === task.id) {
            return data;
          }
          return t;
        });
        setTasks(updatedTasks);
      })
      .catch((error) => console.error('Error updating task:', error));
  }

  const handleDelete = (taskId) => {
    console.log('Delete task:', taskId);
  }

  console.log(tasks);

  return (
    <>
    <Header/>
    <Form addTask={addTask}/>
    <TaskContainer tasks={tasks} handleEdit={handleEdit}/>
    </>
    
  );
}

export default App;
