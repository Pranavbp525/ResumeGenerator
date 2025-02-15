```mermaid
graph TD
    subgraph "User Input"
        A[User YAML Resume Data]
        C[Raw Job Description JD]
    end

    subgraph "Job Description Analysis"
        B{{Job Description Analyzer GPT-4 Omni}}
        C --> B
        A --> B  
        B --> D["Structured JD Analysis JSON"]
    end

    subgraph "Resume Scoring and Optimization"
        A --> E{{Relevance Scorer GPT-4 Turbo}}
        D --> E
        E --> F["Content Scores & Critical Issues JSON"]
        F --> G{{Content Optimizer Custom GPT-4}}
        G --> H["Optimized Bullet Points JSON"]
    end

    subgraph "Final Review and Output"
        H --> I{{Final Reviewer GPT-4 w/ Constitutional AI}}
        I --> J{ATS Readiness Check}
        J -- "🚨 Corrections Needed" --> G  
        J -- "🟢 ATS Ready" --> K[Templating Engine]
        K --> L["ATS-Crushing Resume PDF"]
    end

    style A fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style B fill:#f9f,stroke:#333,stroke-width:2px
    style D fill:#ffd,stroke:#333,stroke-width:2px
    style E fill:#f9f,stroke:#333,stroke-width:2px
    style F fill:#ffd,stroke:#333,stroke-width:2px
    style G fill:#f9f,stroke:#333,stroke-width:2px
    style H fill:#ffd,stroke:#333,stroke-width:2px
    style I fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#dfd,stroke:#333,stroke-width:2px
    style K fill:#ccf,stroke:#333,stroke-width:2px
    style L fill:#dfd,stroke:#333,stroke-width:2px
