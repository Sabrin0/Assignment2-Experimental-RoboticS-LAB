; Auto-generated. Do not edit!


(cl:in-package exp_assignment2-msg)


;//! \htmlinclude BallState.msg.html

(cl:defclass <BallState> (roslisp-msg-protocol:ros-message)
  ((BallDetected
    :reader BallDetected
    :initarg :BallDetected
    :type cl:boolean
    :initform cl:nil)
   (currentRadius
    :reader currentRadius
    :initarg :currentRadius
    :type cl:float
    :initform 0.0))
)

(cl:defclass BallState (<BallState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <BallState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'BallState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name exp_assignment2-msg:<BallState> is deprecated: use exp_assignment2-msg:BallState instead.")))

(cl:ensure-generic-function 'BallDetected-val :lambda-list '(m))
(cl:defmethod BallDetected-val ((m <BallState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader exp_assignment2-msg:BallDetected-val is deprecated.  Use exp_assignment2-msg:BallDetected instead.")
  (BallDetected m))

(cl:ensure-generic-function 'currentRadius-val :lambda-list '(m))
(cl:defmethod currentRadius-val ((m <BallState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader exp_assignment2-msg:currentRadius-val is deprecated.  Use exp_assignment2-msg:currentRadius instead.")
  (currentRadius m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <BallState>) ostream)
  "Serializes a message object of type '<BallState>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'BallDetected) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'currentRadius))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <BallState>) istream)
  "Deserializes a message object of type '<BallState>"
    (cl:setf (cl:slot-value msg 'BallDetected) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'currentRadius) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<BallState>)))
  "Returns string type for a message object of type '<BallState>"
  "exp_assignment2/BallState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'BallState)))
  "Returns string type for a message object of type 'BallState"
  "exp_assignment2/BallState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<BallState>)))
  "Returns md5sum for a message object of type '<BallState>"
  "5ead8a4581df1f9430fd7170d4a41e9e")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'BallState)))
  "Returns md5sum for a message object of type 'BallState"
  "5ead8a4581df1f9430fd7170d4a41e9e")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<BallState>)))
  "Returns full string definition for message of type '<BallState>"
  (cl:format cl:nil "bool BallDetected~%float64 currentRadius~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'BallState)))
  "Returns full string definition for message of type 'BallState"
  (cl:format cl:nil "bool BallDetected~%float64 currentRadius~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <BallState>))
  (cl:+ 0
     1
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <BallState>))
  "Converts a ROS message object to a list"
  (cl:list 'BallState
    (cl:cons ':BallDetected (BallDetected msg))
    (cl:cons ':currentRadius (currentRadius msg))
))
