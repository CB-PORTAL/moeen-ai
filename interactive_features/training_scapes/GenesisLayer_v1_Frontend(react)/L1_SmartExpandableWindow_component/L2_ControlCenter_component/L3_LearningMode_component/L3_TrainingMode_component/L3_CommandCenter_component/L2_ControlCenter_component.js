import React from 'react';
import './ControlCenterComponent.css';

function ControlCenterComponent() {
    return (
        <div className="control-center">
            <button className="control-button">LearningModeComponent</button>
            <button className="control-button">TrainingModeComponent</button>
            <button className="control-button">CommandCenterComponent</button>
            <button className="control-button">SessionsWindowComponent</button>
            <button className="control-button">AccountSettingsComponent</button>
            <button className="control-button">AskMoeenComponent</button>
        </div>
    );
}

export default ControlCenterComponent;