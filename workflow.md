graph TD
    subgraph User Input
        A[User Resume (YAML/Text)]
        B[Job Description (Text)]
        C[Target Salary Range (Optional)]
    end

    subgraph Job Description Analyzer (JDA)
        D{{JDA - Core Requirements}} --> D1[JSON: core_requirements]
        E{{JDA - Company Values}} --> E1[JSON: company_values]
        F{{JDA - Related Terms}} --> F1[JSON: related_terms]
        G{{JDA - Job Details}} --> G1[JSON: job_details]
        H{{JDA - Confidence Levels}} --> H1[JSON: requirement_confidence]
    end
      
    B --> D
    B --> E
    B --> F
    B --> G
    B --> H

    subgraph Relevance Scorer (RS)
        I{{RS - Phrase Bonus}} --> I1[JSON: phrase_matches]
        J{{RS - Role Complexity}} --> J1[JSON: role_complexity]
        K{{RS - Role Title Relevance}} --> K1[JSON: role_title_relevance]
        L{{RS - Near Miss Dealbreakers}} --> L1[JSON: near_misses]
        M{{RS - Section Scores}} --> M1[JSON: section_scores]
        N{{RS - Total Score Calculation}} --> N1[Float: total_score]
    end

    A --> I
    B --> I
    A --> J
    A --> K
    B["Job Title (from G1)"] --> K
    A --> L
    B --> L
    A --> M
    D1 --> M
    F1 --> M
    J1 --> M
    K1 --> M
    M --> N

    subgraph Content Optimizer (CO)
        O{{CO - ATS Keyword Injection & STAR}} --> O1[JSON: optimized_bullets]
        P{{CO - Strategic Padding}} --> P1[JSON: optimized_bullets (w/ padding_flag)]
    end

    A --> O
    M1 --> O
    D1 --> O
    F1 --> O
    L1 --> P
    A --> P
    O --> P1
    O --> O1

    subgraph Final Reviewer (FR)
        Q{{FR - Keyword Ratio Check}} --> Q1[JSON: keyword_ratio_check]
        R{{FR - Metrics Check}} --> R1[JSON: metrics_check]
        S{{FR - Dealbreaker Check}} --> S2[JSON: dealbreaker_status]
        T{{FR - Style & Grammar Check}} --> T1[JSON: style_check]
        U{{FR - Estimated Metrics}} --> U1[JSON: optimized_bullets (w/ metrics_source)]
        V{{FR - Overall Assessment}} --> V1[JSON: final_assessment]
    end

    P1 --> Q
    O1 --> Q
    D1 --> Q
    F1 --> Q
    P1 --> R
    O1 --> R
    P1 --> S
    O1 --> S
    L1 --> S
    P1 --> T
    O1 --> T
    P1 --> U
    P1 --> V
    O1 --> V
    Q1 --> V
    R1 --> V
    S2 --> V
    T1 --> V
    U1 --> V

     subgraph Salary Booster (SB - Optional)
        W{{SB - Salary Optimization}} --> W1[Revised Resume Text]
    end
    
    V1 --> W
    B --> W
    C --> W


    subgraph Output
        X[Templating Engine] --> Y[ATS-Optimized Resume (PDF/DOCX)]
    end

    V1 --> X
    W1 --> X  ; If Salary Booster is used.
    
    linkStyle 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43 stroke:#000,stroke-width:1px
    linkStyle 15,23,32,36,42 stroke:#f00,stroke-width:2px