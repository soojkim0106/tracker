import "../css/TaskCard.css";

const TaskCard = ({ task, onEdit, onDelete, onCompleteTask }) => {
  const { id, title, description, status } = task;
  const statusClass = status.toLowerCase().replace(" ", "-");


  return (
    <div className={`task-card ${statusClass}`}>
      <div className="task-content">
        <div className="task-item">
          <strong>Title:</strong> {title}
        </div>
        <div className="description">
          <strong>| Description:</strong> {description}
        </div>
      </div>
      <div className="task-actions">
        {status !== 'Completed' && (
          <button className="task-done-button" onClick={onCompleteTask}>
            <i className="fa-solid fa-circle-check"></i>
          </button>
        )}
        <button className="task-edit-button" onClick={onEdit}>
          <i className="fa-solid fa-pencil"></i>
        </button>
        <button className="task-delete-button" onClick={onDelete}>
          <i className="fa-solid fa-trash-can"></i>
        </button>
      </div>
    </div>
  );
};

export default TaskCard;
