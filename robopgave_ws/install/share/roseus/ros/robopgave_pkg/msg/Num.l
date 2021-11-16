;; Auto-generated. Do not edit!


(when (boundp 'robopgave_pkg::Num)
  (if (not (find-package "ROBOPGAVE_PKG"))
    (make-package "ROBOPGAVE_PKG"))
  (shadow 'Num (find-package "ROBOPGAVE_PKG")))
(unless (find-package "ROBOPGAVE_PKG::NUM")
  (make-package "ROBOPGAVE_PKG::NUM"))

(in-package "ROS")
;;//! \htmlinclude Num.msg.html


(defclass robopgave_pkg::Num
  :super ros::object
  :slots (_question _answer ))

(defmethod robopgave_pkg::Num
  (:init
   (&key
    ((:question __question) "")
    ((:answer __answer) "")
    )
   (send-super :init)
   (setq _question (string __question))
   (setq _answer (string __answer))
   self)
  (:question
   (&optional __question)
   (if __question (setq _question __question)) _question)
  (:answer
   (&optional __answer)
   (if __answer (setq _answer __answer)) _answer)
  (:serialization-length
   ()
   (+
    ;; string _question
    4 (length _question)
    ;; string _answer
    4 (length _answer)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _question
       (write-long (length _question) s) (princ _question s)
     ;; string _answer
       (write-long (length _answer) s) (princ _answer s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _question
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _question (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _answer
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _answer (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get robopgave_pkg::Num :md5sum-) "a27d8629aeefd2b315942fe4a74ab143")
(setf (get robopgave_pkg::Num :datatype-) "robopgave_pkg/Num")
(setf (get robopgave_pkg::Num :definition-)
      "string question
string answer

")



(provide :robopgave_pkg/Num "a27d8629aeefd2b315942fe4a74ab143")


