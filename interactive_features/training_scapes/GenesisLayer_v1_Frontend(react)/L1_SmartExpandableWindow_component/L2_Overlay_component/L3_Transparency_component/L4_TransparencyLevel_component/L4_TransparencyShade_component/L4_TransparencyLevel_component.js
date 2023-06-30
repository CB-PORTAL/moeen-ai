import React from 'react';
import './TransparencyLevel.css';

function TransparencyLevel({ level }) {
    return (
        <div className="transparency-level" style={{ opacity: level }}>
            {/* Content goes here... */}
        </div>
    );
}

export default TransparencyLevel;