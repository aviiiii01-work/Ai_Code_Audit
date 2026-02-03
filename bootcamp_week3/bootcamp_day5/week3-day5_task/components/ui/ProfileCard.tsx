import React from 'react';
import Card from './Card';

interface ProfileCardProps {
  name: string;
  email: string;
  role: string;
}

const ProfileCard: React.FC<ProfileCardProps> = ({ name, email, role }) => {
  return (
    <Card>
      <h2 className="text-xl font-bold mb-2">{name}</h2>
      <p className="mb-1"><strong>Email:</strong> {email}</p>
      <p><strong>Role:</strong> {role}</p>
    </Card>
  );
};

export default ProfileCard;
