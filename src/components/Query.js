import React, {useState} from 'react';

const Input = (input) => {
  const [state,setState] = useState("");
    return (
      <React.Fragment>
        <div className="controls">
          <input
            type="text"
            className="query-input"
            data-testid="query-input"
            value={state}
            onChange={(e) => setState(e.target.value)}
          />
        </div>
      </React.Fragment>
    );
  };

export default Input;
