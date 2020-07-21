import React from 'react';
import { List, Header } from "semantic-ui-react";


export const Pitches = ({ pitches }) => {
  return (
    <List>
     {pitches.map(pitch => {
       return (
         <List.Item key={pitch.index}>
          <Header>{pitch.pitchType}: {pitch.avg_endSpeed}</Header>
         </List.Item>
       )
     })}
    </List>
  )
};
