import React from 'react';
import './TaskCard.css';

const TaskCard = ({ task, onEdit, onDelete }) => {
  const { title, description, status } = task;

  const statusClass = status.toLowerCase().replace(' ', '-');

  return (
    <div className={`task-card ${statusClass}`}>
      <div className="task-content">
        <p>{title}</p>
        <p>{description}</p>
        <p>{status}</p>
      </div>
      <div className="task-actions">
        <button onClick={() => onEdit(task)}>Edit</button>
        <button onClick={() => onDelete(task.id)}>Delete</button>
      </div>
    </div>
  );
};

export default TaskCard;