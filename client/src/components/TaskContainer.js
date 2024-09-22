import { useState, useEffect } from 'react';
import TaskCard from './TaskCard';
import Modal from './Modal';

const TaskList = ({ tasks }) => {
  const [taskList, setTaskList] = useState(tasks);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedTask, setSelectedTask] = useState(null);

  useEffect(() => {
    console.log('Initial tasks:', tasks);
    setTaskList(tasks);
  }, [tasks]);

  const handleEdit = (task) => {
    setSelectedTask(task);
    setIsModalOpen(true);
  };

  const handleDelete = (taskId) => {
    const confirmDelete = window.confirm('Are you sure you want to delete this task?');
    if (confirmDelete){
      fetch(`http://localhost:5555/tasks/${taskId}`, {
        method: 'DELETE'
      })
        .then(() => console.log('Task deleted:', taskId))
        .catch((error) => console.error('Error deleting task:', error));
    }
  };

  const handleFormSubmit = (updatedTask) => {
    fetch(`http://localhost:5555/tasks/${updatedTask.id}`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(updatedTask)
    })
      .then((response) => response.json())
      .then((data) => {
        console.log('Task updated:', data);
        setTaskList(taskList.map(task => task.id === data.id ? data : task));
        setIsModalOpen(false);
      })
      .catch((error) => console.error('Error updating task:', error));
  };

  return (
    <div>
      {taskList.length === 0 ? (
        <p>No tasks available</p>
      ) : (
        taskList.map(task => (
          <TaskCard
            key={task.id}
            task={task}
            onEdit={handleEdit}
            onDelete={handleDelete}
          />
        ))
      )}
      <Modal isOpen={isModalOpen} onClose={() => setIsModalOpen(false)}>
        {selectedTask && (
          <form onSubmit={(e) => {
            e.preventDefault();
            handleFormSubmit({
              ...selectedTask,
              title: e.target.title.value,
              description: e.target.description.value,
              status: e.target.status.value
            });
          }}>
            <div>
              <label htmlFor="title">Title:</label>
              <input
                type="text"
                id="title"
                name="title"
                defaultValue={selectedTask.title}
                required
              />
            </div>
            <div>
              <label htmlFor="description">Description:</label>
              <textarea
                id="description"
                name="description"
                defaultValue={selectedTask.description}
                required
              />
            </div>
            <div>
              <label htmlFor="status">Status:</label>
              <select
                id="status"
                name="status"
                defaultValue={selectedTask.status}
                required
              >
                <option value="Not Started">Not Started</option>
                <option value="In Progress">In Progress</option>
                <option value="Completed">Completed</option>
              </select>
            </div>
            <button type="submit">Save</button>
          </form>
        )}
      </Modal>
    </div>
  );
};

export default TaskList;