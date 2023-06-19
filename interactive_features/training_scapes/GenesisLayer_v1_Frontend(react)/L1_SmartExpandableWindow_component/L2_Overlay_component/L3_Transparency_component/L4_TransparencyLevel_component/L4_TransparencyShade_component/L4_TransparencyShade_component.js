import React from 'react';
import './TransparencyShade.css';

function TransparencyShade({ shade }) {
    return (
        <div className="transparency-shade" style={{ backgroundColor: shade }}>
            {/* Content goes here... */}
        </div>
    );
}

export default TransparencyShade;