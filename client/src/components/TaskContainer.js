import { useState } from 'react';
import TaskCard from './TaskCard';
import Modal from './Modal';
import StatusExplainer from './StatusExplainer';

const TaskContainer = ({ tasks, onUpdateTask, onDeleteTask, onCompleteTask }) => {
  const [selectedTask, setSelectedTask] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleEdit = (task) => {
    setSelectedTask(task);
    setIsModalOpen(true);
  };

  const handleFormSubmit = (updatedTask) => {
    onUpdateTask(updatedTask);
    setIsModalOpen(false);
  };

  const sortTasks = (tasks) => {
    const statusOrder = {
      'Not Started': 1,
      'In Progress': 2,
      'Completed': 3
    };
    return tasks.sort((a, b) => statusOrder[a.status] - statusOrder[b.status]);
  };

  const sortedTasks = sortTasks(tasks);

  return (
    <>
    <div>
      {sortedTasks.length === 0 ? (
        <p>No tasks available</p>
      ) : (
        sortedTasks.map(task => (
          <TaskCard
          key={task.id}
          task={task}
          onEdit={() => handleEdit(task)}
          onDelete={() => onDeleteTask(task.id)}
          onCompleteTask={() => onCompleteTask(task.id)}
          />
        ))
      )}
      {isModalOpen && (
        <Modal
        task={selectedTask}
        onClose={() => setIsModalOpen(false)}
        onSubmit={handleFormSubmit}
        />
      )}
      <StatusExplainer />
    </div>
    </>
  );
};

export default TaskContainer;