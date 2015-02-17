(ns role-select.core
  (:gen-class))

(def questions
    ["Do you like protecting your friends? (y/n) => "
    "Do you like being a leader? (y/n) => "
    "Do you like being in the background? (y/n) => "
    "Do you like dealing damage up close? (y/n) => "
    "Far away? (y/n) => "
    "Do you like working alone? (y/n) => "
    "Do you like melee? (y/n) => "
    "Ranged? (y/n) => "])

(defn print-questions [questions]
  (reduce (fn [answer question]
    (println question)
    (if (= "y" (read-line))
      (inc answer)
          answer))
          0
          questions))

(defn -main [& args]
  (let [number (print-questions questions)]
    (println number)))
