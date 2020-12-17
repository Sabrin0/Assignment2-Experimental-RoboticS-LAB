;; Auto-generated. Do not edit!


(when (boundp 'exp_assignment2::BallState)
  (if (not (find-package "EXP_ASSIGNMENT2"))
    (make-package "EXP_ASSIGNMENT2"))
  (shadow 'BallState (find-package "EXP_ASSIGNMENT2")))
(unless (find-package "EXP_ASSIGNMENT2::BALLSTATE")
  (make-package "EXP_ASSIGNMENT2::BALLSTATE"))

(in-package "ROS")
;;//! \htmlinclude BallState.msg.html


(defclass exp_assignment2::BallState
  :super ros::object
  :slots (_BallDetected _currentRadius ))

(defmethod exp_assignment2::BallState
  (:init
   (&key
    ((:BallDetected __BallDetected) nil)
    ((:currentRadius __currentRadius) 0.0)
    )
   (send-super :init)
   (setq _BallDetected __BallDetected)
   (setq _currentRadius (float __currentRadius))
   self)
  (:BallDetected
   (&optional __BallDetected)
   (if __BallDetected (setq _BallDetected __BallDetected)) _BallDetected)
  (:currentRadius
   (&optional __currentRadius)
   (if __currentRadius (setq _currentRadius __currentRadius)) _currentRadius)
  (:serialization-length
   ()
   (+
    ;; bool _BallDetected
    1
    ;; float64 _currentRadius
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _BallDetected
       (if _BallDetected (write-byte -1 s) (write-byte 0 s))
     ;; float64 _currentRadius
       (sys::poke _currentRadius (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _BallDetected
     (setq _BallDetected (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float64 _currentRadius
     (setq _currentRadius (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get exp_assignment2::BallState :md5sum-) "5ead8a4581df1f9430fd7170d4a41e9e")
(setf (get exp_assignment2::BallState :datatype-) "exp_assignment2/BallState")
(setf (get exp_assignment2::BallState :definition-)
      "bool BallDetected
float64 currentRadius



")



(provide :exp_assignment2/BallState "5ead8a4581df1f9430fd7170d4a41e9e")


