; Auto-generated. Do not edit!


(cl:in-package exp_assignment2-msg)


;//! \htmlinclude PlanningBallResult.msg.html

(cl:defclass <PlanningBallResult> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass PlanningBallResult (<PlanningBallResult>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlanningBallResult>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlanningBallResult)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name exp_assignment2-msg:<PlanningBallResult> is deprecated: use exp_assignment2-msg:PlanningBallResult instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlanningBallResult>) ostream)
  "Serializes a message object of type '<PlanningBallResult>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlanningBallResult>) istream)
  "Deserializes a message object of type '<PlanningBallResult>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlanningBallResult>)))
  "Returns string type for a message object of type '<PlanningBallResult>"
  "exp_assignment2/PlanningBallResult")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanningBallResult)))
  "Returns string type for a message object of type 'PlanningBallResult"
  "exp_assignment2/PlanningBallResult")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlanningBallResult>)))
  "Returns md5sum for a message object of type '<PlanningBallResult>"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlanningBallResult)))
  "Returns md5sum for a message object of type 'PlanningBallResult"
  "d41d8cd98f00b204e9800998ecf8427e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlanningBallResult>)))
  "Returns full string definition for message of type '<PlanningBallResult>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlanningBallResult)))
  "Returns full string definition for message of type 'PlanningBallResult"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlanningBallResult>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlanningBallResult>))
  "Converts a ROS message object to a list"
  (cl:list 'PlanningBallResult
))
